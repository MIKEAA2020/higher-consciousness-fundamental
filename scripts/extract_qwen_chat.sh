#!/bin/bash
# Extract all 60 messages from the rendered Qwen shared chat into a single JSONL file
OUT=/home/z/my-project/qwen_messages.jsonl
> "$OUT"

for i in $(seq 0 59); do
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
done
echo "DONE - $(wc -l < $OUT) lines"
