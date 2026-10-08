#!/usr/bin/env python3
"""Extract attached-file metadata + signed URLs from the ds3 share payload."""
import json

PATH = "/home/z/my-project/glm agent 2/research/ds3_share_content.json"

with open(PATH, "r", encoding="utf-8") as f:
    raw = f.read()

# The file may be the raw JSON string of the API response body.
data = json.loads(raw)
# The saved payload in round 9 was the response body: {"code":0,...,"data":{...}}
if isinstance(data, dict) and "data" in data:
    biz = data.get("data", {})
    if isinstance(biz, dict) and "biz_data" in biz:
        biz = biz["biz_data"]
else:
    biz = data

msgs = biz.get("messages", [])
print(f"messages: {len(msgs)}")
for m in msgs:
    for frag in (m.get("fragments") or []):
        if frag.get("type") == "FILE":
            for fmeta in frag.get("files", []):
                print("=" * 60)
                for k in ("file_name", "file_size", "token_usage", "status", "is_image", "inserted_at"):
                    print(f"  {k}: {fmeta.get(k)}")
                sp = fmeta.get("signed_path", "")
                print(f"  signed_path: {sp}")

# also dump every http(s) URL appearing anywhere in the payload
import re
urls = sorted(set(re.findall(r'https?://[^\s"\\]+', raw)))
print("\nALL URLS IN PAYLOAD:")
for u in urls:
    print(" ", u[:160])
