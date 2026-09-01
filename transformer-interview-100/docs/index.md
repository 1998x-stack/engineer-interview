# Transformer Interview 100 · Professional Edition

> 面向 **NLP / LLM / 搜索推荐 / 多模态 / ML Systems 算法岗** 的 Transformer 专项知识库。主线不是背 100 个答案，而是训练从 **定义 → 数学 → Tensor Shape → 数值稳定性 → 代码 → GPU/Serving → 验证** 的连续推导能力。

## 你会得到什么

- **Q001–Q100**：每题一个独立 Markdown；
- 每题保留 `PDF Core`，并增加题目特异的 `Professional Expansion`；
- 公式、shape、参数量/FLOPs、activation/KV memory、HBM/通信视角；
- Coding/Debug 的 reference / invariant / parity 测试方法；
- 10 个 System Design 深挖案例；
- 公式速查、30 个工程 Gotchas、论文阅读路径；
- MkDocs + GitHub Pages + CI 文档完整性检查。

## 三种使用模式

### 1. 面试冲刺

从 [100 题索引](guide/question-index.md) 开始，只读：

`30 秒回答 → 核心公式/Shape → 常见失分点 → 追问`

目标：每题 60 秒内稳定说出主干。

### 2. 深度学习

先读 [知识地图](guide/knowledge-map.md)，再按章节完成：

`手推 → 手算 → Coding → Test → Profiler/Ablation`

目标：能解释为什么一个变体在某些条件下更好、某些条件下反而更差。

### 3. 高级算法 / ML Systems

重点刷：

- Q019：Attention 成本；
- Q029–Q034：RoPE / 长上下文；
- Q057–Q066：训练稳定性与并行；
- Q068–Q080：KV Cache / Serving；
- Q081–Q090：FlashAttention / MoE / Quantization；
- Q091–Q100：Coding / Debug / Design。

并完成 [System Design](system-design/SD02.md)。

## 推荐入口

| 目标 | 页面 |
|---|---|
| 看全题 | [100 题索引](guide/question-index.md) |
| 建知识树 | [知识地图](guide/knowledge-map.md) |
| 学会表达 | [六层回答法](guide/six-layer-answer.md) |
| 30 天训练 | [30 天路径](guide/30-day-plan.md) |
| 考前速查 | [公式手册](appendix/formula-cheatsheet.md) |
| 排雷 | [30 个 Gotchas](appendix/gotchas.md) |
| 深挖论文 | [论文地图](reference/papers.md) |

## 内容层级

### PDF Core

保留参考 PDF 的题目、考察点、30 秒答案、主推导、失分点与追问。仓库不会静默修改这部分的核心结论。

### Professional Expansion

原创补充：

- 更严格的成立条件；
- 数学/shape 推导；
- 训练 vs prefill vs decode；
- kernel / HBM / NCCL；
- 反例与边界；
- correctness/performance/quality 三类验证。

## 质量原则

1. **不把经验写成定律**：性能结论必须带 workload / hardware 条件。
2. **不把 Big-O 写成 wall-clock**：同时看 IO、kernel、通信。
3. **不把运行成功当正确**：优先行为测试与 oracle parity。
4. **不把 max context 当有效 context**：长上下文必须位置分桶评测。
5. **不把论文名字当答案**：未知变体也要能从 shape/公式重新推导。

## 原始参考 PDF

`assets/reference/Transformer_算法岗面试100题_专业版.pdf`
