# Book / PDF release

这里保存 **LLM Pretraining Interview 100** 的版式化书稿与可发行 PDF：

- [`LLM-Pretraining-Interview-100.pdf`](./LLM-Pretraining-Interview-100.pdf)：A4，93 页，100 道题完整 PDF；
- `llm_pretrain_offer.html`：PDF 的排版源文件；
- `llm_pretrain_100.jsonl`：PDF 主体 100 题的结构化内容；
- `CONTENT_MAP.md`：书稿内容映射。

## PDF 与 Markdown 的职责

PDF 适合连续阅读、打印、集中复习；`questions/` 是更细粒度、持续演进的知识库，在书稿基础上进一步扩充了工程实验、追问方向、评分 Rubric、自测和最新官方资料。

因此项目采用双轨维护：

```text
book/*.jsonl + book/*.html
          │
          ├──> PDF：稳定、可打印的书稿发行物
          │
          └──> questions/*.md：逐题深化、持续维护
```

## 重新生成 PDF

在 Repo 根目录执行：

```bash
python scripts/build_pdf.py
```

默认输出：`book/LLM-Pretraining-Interview-100.pdf`。
