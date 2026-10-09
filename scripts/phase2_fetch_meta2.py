#!/usr/bin/env python3
"""Fetch metadata files via the working S3 route for all four corpora."""
import subprocess
import os

OUT = "/home/z/my-project/glm agent 2/research/phase2/meta"
os.makedirs(OUT, exist_ok=True)

FILES = [
    ("ds004541", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_events.tsv"),
    ("ds004541", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_events.json"),
    ("ds004541", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_eeg.json"),
    ("ds004541", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_channels.tsv"),
    ("ds004541", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_eeg.edf"),
    ("ds004541", "sub-04/ses-01/eeg/sub-04_ses-01_task-anesthesia_events.tsv"),
    ("ds004541", "sub-11/ses-01/eeg/sub-11_ses-01_task-anesthesia_events.tsv"),
    ("ds004541", "participants.json"),
    ("ds005620", "sub-1010/eeg/sub-1010_task-awake_acq-EC_eeg.json"),
    ("ds005620", "sub-1010/eeg/sub-1010_task-awake_acq-EC_eeg.vhdr"),
    ("ds003171", "sub-02CB/func/sub-02CB_task-restdeep_run-01_bold.json"),
    ("ds006623", "sub-02/sub-02_task-imagery_bold.json"),
    ("ds006623", "sub-02/sub-02_task-rest_bold.json"),
]

for dsid, path in FILES:
    url = f"https://s3.amazonaws.com/openneuro.org/{dsid}/{path}"
    dest = os.path.join(OUT, f"{dsid}__{path.replace('/', '__')}")
    # HEAD-style range probe for big files: only fetch first 1 KB of .edf/.vhdr
    if path.endswith(".edf"):
        r = subprocess.run(["curl", "-sS", "-L", "-m", "90", "-r", "0-2047", "-o", dest,
                            "-w", "%{http_code} %{size_download}", url],
                           capture_output=True, text=True, timeout=120)
    else:
        r = subprocess.run(["curl", "-sS", "-L", "-m", "90", "-o", dest,
                            "-w", "%{http_code} %{size_download}", url],
                           capture_output=True, text=True, timeout=120)
    print(r.stdout, path)
