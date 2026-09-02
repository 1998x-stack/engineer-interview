# Repository Structure

```text
llm-inference-interview-100/
├── README.md
├── mkdocs.yml
├── data/
│   └── questions.json              # 100 题机器可读元数据
├── assets/pdf/
│   └── LLM_Inference_Interview_100_2026.pdf
├── sources/
│   └── pdf-extracted.txt           # PDF 原始文本抽取，便于审计
├── docs/
│   ├── index.md
│   ├── knowledge-map.md
│   ├── learning-path.md
│   ├── formula-cheatsheet.md
│   ├── benchmark-playbook.md
│   ├── framework-matrix.md
│   ├── interview-playbook.md
│   ├── top20.md
│   ├── glossary.md
│   ├── chapters/
│   │   ├── 01-performance-fundamentals/  # Q001-Q010
│   │   ├── 02-kv-cache-attention/        # Q011-Q020
│   │   ├── 03-batching-scheduling/       # Q021-Q030
│   │   ├── 04-kernel-runtime/            # Q031-Q040
│   │   ├── 05-quantization/              # Q041-Q050
│   │   ├── 06-distributed-inference/     # Q051-Q060
│   │   ├── 07-speculative-decoding/      # Q061-Q070
│   │   ├── 08-moe-mla-codesign/          # Q071-Q080
│   │   ├── 09-serving-runtimes/          # Q081-Q090
│   │   └── 10-production-system-design/  # Q091-Q100
│   └── appendices/
│       ├── references.md
│       └── source-notes.md
├── scripts/
│   ├── verify_repo.py
│   └── build_index.py
└── .github/
    ├── workflows/verify.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 设计原则

- **一个问题一个 Markdown**：便于链接、Review、版本演进和知识库导入。
- **章节物理隔离**：目录和知识结构一致。
- **PDF 基线可审计**：原始 PDF 与文本抽取都保留。
- **机器可读**：`questions.json` 可用于生成网站、Anki 或搜索索引。
- **自动校验**：CI 检查 100 题连续性、必要章节和内部链接。
- **版本敏感**：外部框架信息与 PDF 原始内容明确区分。
