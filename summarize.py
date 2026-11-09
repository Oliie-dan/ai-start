import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

text = Path("note.txt").read_text(encoding="utf-8")
print(f"读到 {len(text)} 个字符")

prompt = f"""请用三句话总结下面这段内容的核心意思，再列出三个关键词，用顿号隔开。

正文如下：
{text}"""

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": prompt}],
)

answer = resp.choices[0].message.content
print(answer)

Path("summary.txt").write_text(answer, encoding="utf-8")
print("\n已保存到 summary.txt")