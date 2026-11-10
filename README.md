# ai-start

用 DeepSeek API 做的文本总结小工具：读入一个 txt 文件，输出三句话摘要和三个关键词，结果保存为 summary.txt。

## 怎么跑

1. 复制 `.env.example` 为 `.env`，填入你的 `DEEPSEEK_API_KEY`
2. 安装依赖：`python -m pip install -r requirements.txt`
3. 运行：`python summarize.py`，按提示输入 txt 文件路径

## 输出示例

    读到 268 个字符

    --- 模型输出 ---
    1. 通勤时间是城市生活中最容易被低估的成本……
    2. 真正影响体验的是"可控感"，而不是单纯的距离……
    3. 人们愿意多花点时间，换取对自己节奏的掌控权……

    已保存到 summary.txt

## 用了什么

Python 3.13 · openai SDK · DeepSeek API · 无第三方框架，单文件实现

## 文件说明

- `summarize.py`：主程序，读文件、调模型、存结果
- `batch_summarize.py`：批量版，一次处理多个文件
- `hello.py`：最小调用示例，用来验证 key 是否可用
- `.env.example`：配置模板，复制成 `.env` 后填真实 key