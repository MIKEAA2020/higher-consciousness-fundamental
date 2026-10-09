#!/usr/bin/env python3
"""Phase 2 — ds004541 EEG epoch extraction via EDF range requests.

Fetches (per session): events.tsv, EDF header; computes epoch byte-ranges;
range-requests only the epochs needed; parses int16 -> uV; drops bad
channels; average-references; decimates to 250 Hz; saves npz.

Epochs (from events.tsv trial_types):
  pre        [baseline or 0 .. start]        awake baseline
  induction  [start .. loc]                  descending (optional)
  maintenance[max(loc,start)+45 .. end-45]   deep GA
  emergence  [end+30 .. roc-30]              transition
  recovery   [roc+30 .. roc+270]             awake again
Minimum usable duration: 120 s (else skipped).
"""
import json
import os
import re
import subprocess
import numpy as np

OUT = "/home/z/my-project/glm agent 2/research/phase2/ds004541"
os.makedirs(OUT, exist_ok=True)
BASE = "https://s3.amazonaws.com/openneuro.org/ds004541"

SESSIONS = [
    "sub-02/ses-01", "sub-03/ses-01", "sub-04/ses-01", "sub-07/ses-01",
    "sub-08/ses-01", "sub-09/ses-01", "sub-10/ses-01", "sub-11/ses-01",
    "sub-11/ses-02",
]


def curl(url, dest, rng=None):
    cmd = ["curl", "-sS", "-L", "-m", "240"]
    if rng:
        cmd += ["-r", rng]
    cmd += ["-o", dest, "-w", "%{http_code} %{size_download}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    return r.stdout


def fetch_events(sess):
    p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_events.tsv"
    dest = f"{OUT}/{sess.replace('/', '_')}_events.tsv"
    out = curl(f"{BASE}/{p}", dest)
    ev = {}
    with open(dest) as f:
        next(f)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                ev[parts[2]] = float(parts[0])
    return ev, out


def fetch_edf_header(sess):
    p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_eeg.edf"
    dest = f"{OUT}/{sess.replace('/', '_')}_edfheader.bin"
    out = curl(f"{BASE}/{p}", dest, rng="0-18175")
    return dest


def parse_edf_header(path):
    raw = open(path, "rb").read()
    hdr_bytes = int(raw[184:192].decode().strip())
    n_rec = int(raw[236:244].decode().strip())
    rec_dur = float(raw[244:252].decode().strip())
    n_sig = int(raw[252:256].decode().strip())
    labels, sprs, phys_min, phys_max, dig_min, dig_max = [], [], [], [], [], []
    # EDF signal-header layout (256 B each): label[0:16], transducer[16:80],
    # physdim[80:88], physmin[88:96], physmax[96:104], digmin[104:112],
    # digmax[112:120], prefilter[120:144], samples[236:244], reserved[248:256]
    for i in range(n_sig):
        b = raw[256 + i * 256: 256 + (i + 1) * 256]
        labels.append(b[0:16].decode().strip())
        sprs.append(int(b[236:244].decode().strip()))
        phys_min.append(float(b[88:96].decode().strip()))
        phys_max.append(float(b[96:104].decode().strip()))
        dig_min.append(float(b[104:112].decode().strip()))
        dig_max.append(float(b[112:120].decode().strip()))
    recbytes = sum(sprs) * 2
    return dict(hdr_bytes=hdr_bytes, n_rec=n_rec, rec_dur=rec_dur, n_sig=n_sig,
                labels=labels, sprs=sprs, phys_min=phys_min, phys_max=phys_max,
                dig_min=dig_min, dig_max=dig_max, recbytes=recbytes)


def fetch_epoch(sess, hdr, t0, t1, tmp="/tmp/edf_chunk.bin"):
    p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_eeg.edf"
    r0 = int(np.floor(t0 / hdr["rec_dur"]))
    r1 = int(np.ceil(t1 / hdr["rec_dur"]))
    r1 = min(r1, hdr["n_rec"])
    b0 = hdr["hdr_bytes"] + r0 * hdr["recbytes"]
    b1 = hdr["hdr_bytes"] + r1 * hdr["recbytes"] - 1
    out = curl(f"{BASE}/{p}", tmp, rng=f"{b0}-{b1}")
    nrec = r1 - r0
    raw = np.fromfile(tmp, dtype="<i2")
    expected = nrec * hdr["recbytes"] // 2
    raw = raw[:expected]
    # demultiplex: (nrec, totalspr)
    totalspr = sum(hdr["sprs"])
    raw = raw.reshape(nrec, totalspr)
    # build channel matrix
    chans = []
    offs = np.cumsum([0] + hdr["sprs"])
    for i in range(hdr["n_sig"]):
        if hdr["sprs"][i] == max(hdr["sprs"]) and "EEG" in hdr["labels"][i].upper():
            x = raw[:, offs[i]:offs[i + 1]].astype(np.float64)
            # int16 -> uV
            a = hdr["phys_max"][i] - hdr["phys_min"][i]
            b = hdr["dig_max"][i] - hdr["dig_min"][i]
            x = hdr["phys_min"][i] + (x - hdr["dig_min"][i]) * a / max(b, 1)
            chans.append((hdr["labels"][i], x.T))  # (samples, nrec) -> transpose later
    # assemble (nch, nsamples) at fs = spr_max / rec_dur
    fs = max(hdr["sprs"]) / hdr["rec_dur"]
    names = [c[0] for c in chans]
    data = np.stack([c[1].reshape(-1) for c in chans]) if chans else None
    return names, data, fs, r0 * hdr["rec_dur"]


def decimate(x, fs, target=250.0):
    from scipy.signal import resample_poly
    from math import gcd
    g = gcd(int(round(fs)), int(target))
    up, down = int(target) // g, int(round(fs)) // g
    # resample_poly needs up/down ints; fs here ~1000 -> 250: up=1 down=4
    return resample_poly(x, up, down, axis=1), target


def good_channels(sess, names):
    chf = f"{OUT}/{sess.replace('/', '_')}_channels.tsv"
    p = f"{sess}/eeg/{sess.replace('/', '_')}_task-anesthesia_channels.tsv"
    if not os.path.exists(chf):
        curl(f"{BASE}/{p}", chf)
    status = {}
    with open(chf) as f:
        next(f)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 8:
                status[parts[0].lstrip('\ufeff')] = parts[7]
    return [n for n in names if status.get(n, "good") != "bad"]


def main():
    plan = {}
    for sess in SESSIONS:
        sid = sess.replace("/", "_")
        try:
            ev, evpath = fetch_events(sess)
            hdrpath = fetch_edf_header(sess)
            hdr = parse_edf_header(hdrpath)
            print(f"== {sid}: events={list(ev.keys())} dur={hdr['n_rec']*hdr['rec_dur']:.0f}s "
                  f"fs={max(hdr['sprs'])/hdr['rec_dur']:.0f}Hz nch_sig={hdr['n_sig']}")
            plan[sid] = {"events": ev, "dur": hdr["n_rec"] * hdr["rec_dur"]}
        except Exception as e:
            print(sid, "FAIL", e)
    with open(f"{OUT}/session_plan.json", "w") as f:
        json.dump(plan, f, indent=1)


if __name__ == "__main__":
    main()
