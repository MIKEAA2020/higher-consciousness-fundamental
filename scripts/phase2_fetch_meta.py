#!/usr/bin/env python3
"""Fetch small metadata files from OpenNeuro for the four anesthesia corpora."""
import subprocess
import os

OUT = "/home/z/my-project/glm agent 2/research/phase2/meta"
os.makedirs(OUT, exist_ok=True)

FILES = [
    ("ds004541", "1.0.0", "README"),
    ("ds004541", "1.0.0", "participants.tsv"),
    ("ds004541", "1.0.0", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_events.tsv"),
    ("ds004541", "1.0.0", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_eeg.json"),
    ("ds004541", "1.0.0", "sub-02/ses-01/eeg/sub-02_ses-01_task-anesthesia_channels.tsv"),
    ("ds004541", "1.0.0", "sub-04/ses-01/eeg/sub-04_ses-01_task-anesthesia_events.tsv"),
    ("ds005620", "1.0.0", "README.txt"),
    ("ds005620", "1.0.0", "participants.tsv"),
    ("ds005620", "1.0.0", "sub-1010/eeg/sub-1010_task-awake_acq-EC_eeg.json"),
    ("ds003171", "2.0.1", "README"),
    ("ds003171", "2.0.1", "participants.tsv"),
    ("ds003171", "2.0.1", "sub-02CB/func/sub-02CB_task-restdeep_run-01_bold.json"),
    ("ds006623", "1.0.0", "README.md"),
    ("ds006623", "1.0.0", "dataset_description.json"),
]

for dsid, tag, path in FILES:
    url = f"https://openneuro.org/crn/datasets/{dsid}/snapshots/{tag}/files/{path}"
    dest = os.path.join(OUT, f"{dsid}__{path.replace('/', '__')}")
    r = subprocess.run(["curl", "-sS", "-L", "-m", "90", "-o", dest, "-w", "%{http_code} %{size_download}", url],
                       capture_output=True, text=True, timeout=120)
    print(r.stdout, path)
