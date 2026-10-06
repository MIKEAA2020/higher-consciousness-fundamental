#!/bin/bash
# Extract all messages from the rendered Qwen shared chat currently open in
# agent-browser (default session) into a JSONL file.
# Usage: extract_qwen_chat2.sh [output.jsonl]   (default: qwen2_messages.jsonl)
# Requires the page to be open with all expand toggles already clicked.
OUT=${1:-/home/z/my-project/qwen2_messages.jsonl}
N=$(agent-browser eval "document.querySelectorAll('.qwen-chat-message').length" 2>/dev/null | tr -d '"')
echo "messages found: $N"
> "$OUT"
for i in $(seq 0 $((N-1))); do
  agent-browser eval "
  (() => {
    const msgs = document.querySelectorAll('.qwen-chat-message');
    const m = msgs[$i];
    if (!m) return JSON.stringify({err: 'no msg ' + $i});
    const isUser = m.classList.contains('qwen-chat-message-user');
    let text = '';
    if (isUser) {
      const c = m.querySelector('.user-message-content');
      text = c ? c.innerText : m.innerText;
    } else {
      const c = m.querySelector('.response-message-content');
      text = c ? c.innerText : m.innerText;
    }
    return JSON.stringify({i: $i, role: isUser ? 'USER' : 'ASSISTANT', text: text});
  })()
  " 2>/dev/null >> "$OUT"
  if (( (i+1) % 11 == 0 )); then echo "  ...$((i+1))/$N extracted"; fi
done
echo "DONE - $(wc -l < $OUT) lines"
