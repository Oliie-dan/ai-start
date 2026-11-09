import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("DEEPSEEK_API_KEY")
if not key:
    raise SystemExit("没读到 key：检查 .env 文件名、位置和拼写")

client = OpenAI(api_key=key, base_url="https://api.deepseek.com")

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话解释什么是 RAG"}],
)

print(resp.choices[0].message.content)