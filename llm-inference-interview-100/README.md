# LLM Deployment & Inference Optimization Interview 100

> 面向算法岗 / AI Infra / LLM Inference & Serving 的 100 题系统化面试手册。  
> **100 questions · 10 chapters · 2026 edition**

本仓库由《LLM 部署与推理优化面试 100 题 · 2026》PDF 拆解并扩展而来。每个问题独立 Markdown，适合 GitHub 阅读、全文检索、Anki/知识库二次加工，以及按章节进行面试训练。

## 仓库不是“100 个名词解释”

整套内容围绕一条主线：

```text
为什么慢
  ↓
慢在哪里（compute / HBM / KV / network / scheduler / CPU）
  ↓
这个优化减少了什么关键路径成本
  ↓
它牺牲了什么
  ↓
哪些 workload 下无效或负优化
  ↓
如何用实验与 profiler 证明
```

每题统一包含：**30 秒回答、考察本质、公式/成本模型、Know-Why、工程场景、建议实验、边界条件、生产 Checklist、Gotchas、追问链、评分标准、2026 工程扩展、延伸阅读、关联题目**。

## 快速开始

- 📘 [在线文档入口](docs/index.md)
- 🗂️ [Repo 结构](docs/repo-structure.md)
- 🗺️ [知识地图](docs/knowledge-map.md)
- 🧭 [学习路线](docs/learning-path.md)
- 🧮 [公式速查](docs/formula-cheatsheet.md)
- 🧪 [Benchmark Playbook](docs/benchmark-playbook.md)
- ⚙️ [vLLM / SGLang / TensorRT-LLM 选型矩阵](docs/framework-matrix.md)
- 🎯 [Top 20 高频题](docs/top20.md)
- 🗣️ [面试答题模板](docs/interview-playbook.md)
- 📖 [术语表](docs/glossary.md)
- 📄 [原始 PDF](assets/pdf/LLM_Inference_Interview_100_2026.pdf)

## 10 大章节

| 章节 | 范围 | 核心能力 |
|---|---|---|
| 01 推理性能基本原理 | Q001-Q010 | Prefill/Decode、Roofline、SLO、估算 |
| 02 KV Cache 与 Attention | Q011-Q020 | KV 显存、PagedAttention、Prefix、GQA/MLA |
| 03 Batching 与 Scheduling | Q021-Q030 | Continuous Batching、Chunked Prefill、Goodput、P/D |
| 04 CUDA / Kernel / Runtime | Q031-Q040 | FlashAttention、Fusion、CUDA Graph、Profiling |
| 05 量化与低精度 | Q041-Q050 | GPTQ、AWQ、SmoothQuant、FP8/FP4、KV Quant |
| 06 分布式推理 | Q051-Q060 | TP/PP/DP/EP/CP、NCCL、拓扑 |
| 07 Speculative Decoding | Q061-Q070 | draft-verify、acceptance、Medusa/EAGLE/MTP |
| 08 MoE / MLA / Co-design | Q071-Q080 | All-to-All、expert balance、MLA、现代 MoE |
| 09 Serving Runtimes | Q081-Q090 | vLLM、SGLang、TensorRT-LLM |
| 10 生产与系统设计 | Q091-Q100 | Benchmark、p99、成本、监控、容量与故障定位 |

## 推荐刷题方式

1. **第一遍：一面速刷** - 只看“30 秒回答 + Gotchas”，每题 45-60 秒口述。
2. **第二遍：二面深挖** - 手写公式，做 KV/带宽/通信数量级估算。
3. **第三遍：系统设计** - 重点 Q030/Q060/Q090/Q091-Q100，要求从 SLO 反推架构。
4. **第四遍：实验化** - 每章完成一个 mini-lab，把答案和真实 profiler 指标对齐。

## 内容边界

- `PDF 基线`：由仓库内原始 PDF 直接拆解，保持其术语和结论框架。
- `2026 工程扩展`：基于公开论文和主流框架文档补充，明确与 PDF 基线区分。
- “真题”指**真题级考点**；对无法公开核验的匿名面经，不冒充某公司原题。

## 本地文档站

仓库附带 `mkdocs.yml`。安装 MkDocs Material 后：

```bash
pip install mkdocs-material
mkdocs serve
```

## 完整性校验

```bash
python scripts/verify_repo.py
```

会检查：100 题是否齐全、编号是否连续、front matter 是否存在、内部 Markdown 链接是否有效。

## License

仓库没有替你做最终开源许可证选择。公开发布前请根据你的用途在 `LICENSE.md` 中选择内容与代码许可证。
