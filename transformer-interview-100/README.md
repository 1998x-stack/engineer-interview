# Transformer Interview 100 · Professional Edition

[![Questions](https://img.shields.io/badge/questions-100-brightgreen)](docs/guide/question-index.md)
[![System Design](https://img.shields.io/badge/system--design-10-orange)](docs/system-design/SD01.md)
[![Docs](https://img.shields.io/badge/docs-MkDocs-blue)](#本地预览)
[![CI](https://img.shields.io/badge/CI-docs%20%2B%20tests-informational)](.github/workflows/ci.yml)

一个面向 **NLP / LLM / 搜索推荐 / 多模态 / ML Systems 算法岗** 的 Transformer 深度面试仓库。

它不是“100 个标准答案”的集合，而是一套从：

> **定义 → 数学 → Tensor Shape → 参数/FLOPs → 数值稳定性 → Coding → GPU/Serving → 验证**

连续训练的专项知识库。

## V2 Professional Edition 有什么变化

相较第一版，本版重点消除了“统一模板化扩展”的问题：

- Q001–Q100 **每题都有题目特异的深入推导**；
- 每题增加工程 Checklist、验证协议、边界条件和 Whiteboard/Coding 表达模板；
- 重点题加入具体手算，例如 KV Cache 32K 容量估算；
- 10 个 System Design 从提纲升级为完整设计：需求、公式、容量、瓶颈、评测、监控、回滚；
- 新增 9 个章节导读，明确每章完成标准与自测问题；
- 公式速查升级为参数/shape/数值边界一体化 cheatsheet；
- 30 个 Gotchas 增加按 Shape / Mask / KV / Training / Systems 的排查法；
- 论文页升级为分层阅读路线，而不是简单链接清单；
- 清理本地 cache/`__pycache__` 等不应提交的产物；
- 保留自动完整性、链接和 pytest 检查。

## Repository Layout

```text
transformer-interview-100/
├── README.md
├── CONTRIBUTING.md
├── REPO_MANIFEST.md
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── guide/
│   │   ├── how-to-use.md
│   │   ├── knowledge-map.md
│   │   ├── six-layer-answer.md
│   │   ├── 30-day-plan.md
│   │   └── question-index.md
│   ├── questions/
│   │   ├── chapter-01/index.md + Q001...Q010
│   │   ├── ...
│   │   └── chapter-09/index.md + Q091...Q100
│   ├── system-design/
│   │   └── SD01...SD10
│   ├── appendix/
│   │   ├── formula-cheatsheet.md
│   │   └── gotchas.md
│   └── reference/papers.md
├── examples/
├── tests/
├── scripts/
├── data/questions.json
├── assets/reference/
└── .github/workflows/
```

## 每道题的结构

题目页保留原 PDF 主干，并在其上增加专业扩展：

1. 面试官在考什么；
2. 30 秒回答；
3. 核心公式 / Shape；
4. PDF Core 深度拆解；
5. Professional Expansion；
6. 面试推导顺序；
7. 常见失分点；
8. 追问树；
9. 一语中的；
10. 评分 Rubric；
11. 相关题；
12. 延伸阅读；
13. **题目特异深入推导**；
14. **工程 Checklist**；
15. **推荐验证协议**；
16. **边界条件**；
17. **Whiteboard / Coding 表达模板**。

## 推荐学习路径

### 面试冲刺

先看：

- [100 题索引](docs/guide/question-index.md)
- [六层回答法](docs/guide/six-layer-answer.md)
- [公式速查](docs/appendix/formula-cheatsheet.md)

每题只练 `30 秒回答 + 3 分钟展开 + 3 层追问`。

### 深度学习

按 [知识地图](docs/guide/knowledge-map.md) 的六条因果链学习，并为每章至少完成：

- 1 次手推；
- 1 次手算；
- 1 个 coding/reference；
- 1 个行为测试；
- 1 个 profiler/ablation 设计。

### LLM Systems / Infra

重点：

`Q068–Q090 + Q091–Q099 + SD02–SD10`

必须掌握：KV Cache、GQA、TTFT/TPOT、PagedAttention、continuous batching、FlashAttention、MoE、quantization、profiling。

## 本地预览

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt
mkdocs serve
```

## Quality Gates

```bash
python scripts/check_docs.py
python scripts/check_links.py
pytest -q
```

建议发布前再执行：

```bash
mkdocs build --strict
```

### 文档质量标准

任何新增/修改题目都应至少满足：

- 公式解释符号与 shape；
- 性能结论说明 workload/hardware 条件；
- 不把 Big-O 等同 wall-clock；
- 至少一个反例/边界；
- 至少一个可执行验证思路；
- Coding/Systems 改动有 correctness regression。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## GitHub Pages

仓库内置 `.github/workflows/docs.yml`。在 GitHub Pages 中选择 **GitHub Actions** 作为部署源即可。

## 内容来源与边界

基础题目与 `PDF Core` 来自项目参考 PDF：

`assets/reference/Transformer_算法岗面试100题_专业版.pdf`

`Professional Expansion` 是在不静默替换 PDF 核心结论的前提下做的原创专业扩展，并参考公开论文。见 [论文地图](docs/reference/papers.md)。

仓库不复制《剑指 Offer》的版权正文或特有版式，只借鉴“题目驱动、逐层分析、举一反三”的学习方法。

## License

发布前请阅读 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)，明确文档与代码许可证。
