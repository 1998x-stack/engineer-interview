# v2 内容增强与质量报告

本仓库的 v2 版本对 Q001–Q100 进行了第二轮专业扩展，目标是从“能回答”提升到“能推导、能实现、能诊断、能做系统决策”。

## 覆盖范围

- 100 / 100 道题均已加入 `第二轮专业扩展（v2）`。
- 每题均包含：
  - 核心机制再拆一层；
  - 数据链路与可复现性；
  - 复杂度、成本与规模感；
  - 白板公式 / 伪代码 / 实验抓手；
  - 失败模式与线上诊断；
  - 可观测性与 Query Slice；
  - Senior / Staff 级追问；
  - 60 / 75 / 85 / 90+ 分层回答标准；
  - 最小可复现实验建议。
- 10 个章节 README 均新增高级面试检查表。
- 修复了若干上一版标题截断问题，例如 WAND、Query Expansion、Cross-Encoder、Refresh Interval 和 Search Cache 题目。

## 内容质量原则

1. **题目特有，而不是统一套模板。** 每题新增一个独立的高级机制焦点，例如 BM25 的极限检查、LambdaRank 的 ΔNDCG、HNSW 的 Recall–Latency 曲线、CDC 的版本化幂等。
2. **公式必须能解释边界。** 数学题要求至少能做极限、反例或数量级检查。
3. **系统必须能算量。** ANN、分布式检索、系统设计题要求讨论内存、候选深度、fan-out、p99、更新或带宽。
4. **离线收益不能直接等价线上收益。** 每题都引入可观测性、slice、guardrail 或 stage-wise diagnosis。
5. **Senior/Staff 看优先级。** 不只回答“用什么算法”，还要解释为何是当前最高 ROI、怎样灰度、怎样回滚、怎样用 oracle / ablation 证明。

## 自动校验

仓库使用 `scripts/validate_repo.py` 校验：

- Q001–Q100 是否连续且恰好 100 题；
- Markdown 内部链接；
- question manifest / metadata；
- 必要章节结构。

同时额外检查：

- 100 题均存在 v2 专业扩展章节；
- Markdown fenced code blocks 成对；
- `mkdocs.yml` 中所有 Markdown nav 路径存在；
- 文本中不存在意外控制字符；
- ZIP 重解压后重新运行完整性验证。

## 建议使用方式

不要从头到尾只读正文。推荐每题执行：

1. 先遮住答案做 30 秒口述；
2. 再用 5 分钟完成公式 / 架构白板；
3. 只看 Senior/Staff 追问继续回答；
4. 完成最小实验，保存 quality–cost 曲线和 bad cases；
5. 最后回到“一句话记忆”做主动提取。
