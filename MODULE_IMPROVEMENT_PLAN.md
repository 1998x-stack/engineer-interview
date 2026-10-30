# Engineer Interview · 逐模块质量改进计划

> 基线：`main`（2026-10-30 审阅）；每轮只修改一个内容模块，并以独立 PR 交付。
> 此表是**审计顺序**，不是未经验证的缺陷断言。除 M01 以外的模块尚待逐一实测。

## 共用验收流程

1. **盘点**：记录模块 HEAD、题目数量、章节/题号、元数据、PDF 与许可文件；不修改既有题号。
2. **复现**：执行已有脚本/测试/MkDocs；记录失败命令与最小复现，不把推断当作已复现。
3. **正确性**：先修公式、算法、边界条件、代码运行错误；对含代码的示例与可信 reference/oracle 对照。
4. **内容**：抽查推导、来源、版本差异、反例、引用；评估重复/空泛模板文本。
5. **质量门禁**：新增回归测试、链接检查、schema 检查、适当的根级 GitHub Actions workflow。
6. **交付**：单模块 PR；提交文件清单、测试结果、未覆盖风险、回滚方式。CI 和 review 通过后再合并。

**不在本轮做的事情**：一次性重命名全站、移动所有 `docs/`/`questions/`、重排题号、自动改写 3,000+ 个答案、未经许可补传参考 PDF。

## M01 — Transformer（本轮）

路径：`transformer-interview-100/`；状态：**修复分支已创建，等待 PR/CI 验证**。

| 问题 | 证据 | 本轮处置 |
| --- | --- | --- |
| 全屏蔽 Attention 行造成 softmax NaN 风险 | `examples/reference_attention.py` 原实现直接使用 `-inf` 计算 softmax | 校验每个 query 至少一个可见 key，否则拒绝 |
| 任意 mask 广播/类型没有契约 | 原 `forward(x, mask)` 不校验形状、dtype | 明确 2D/3D/4D boolean keep-mask 契约 |
| 数值实现仅有两条冒烟测试 | `tests/test_reference_attention.py` | 增加 PyTorch SDPA parity、梯度、非法形状、因果泄漏 |
| 模块内 workflow 不会被 monorepo 直接识别 | `transformer-interview-100/.github/workflows/*` | 新增仓库根级 `.github/workflows/transformer.yml` |
| PDF 引用文件不存在于当前 Git 树 | README/REPO_MANIFEST vs Git tree | README 显式说明不能假设克隆后存在 |

**M01 验收**：本地测试通过；PR CI 完成文档结构、链接、Attention 回归和 MkDocs strict build；独立 reviewer 检查行为变化（所有 key 被屏蔽时改为抛错）。

## 之后的 34 个教程模块

按主 README 的展示次序推进。每轮开始才确定具体 P0/P1 和变更范围，不提前声称存在 bug。

| 顺序 | 模块路径 | 首轮必查重点 |
| --- | --- | --- |
| M02 | `cv-algorithm-interview-handbook-v2` | 检测/OCR/分割指标定义、图像预处理、示例可复现 |
| M03 | `nlp-llm-interview-100` | tokenizer、mask、RAG 检索/评价 |
| M04 | `agent-engineer-interview-100` | 工具权限、状态恢复、prompt 注入与测试 |
| M05 | `deep-learning-interview-100` | 反向传播/优化公式、数值稳定性 |
| M06 | `algorithm-interview-100` | 复杂度、随机/边界用例、题解单测 |
| M07 | `llm-pretraining-interview-100` | scaling、数据去重、并行训练计算 |
| M08 | `llm-inference-interview-100-pro` | KV cache、GQA、batching、算子 parity |
| M09 | `llm-post-training-offer` | DPO/GRPO 推导、reward/评测泄漏 |
| M10 | `search-engine-interview-100` | 索引一致性、BM25/LTR 公式与离线评测 |
| M11 | `recsys_interview_100_repo` | 样本泄漏、召排、在线实验与统计 |
| M12 | `agent-harness-interview-100` | agent loop、超时、隔离、幂等、故障恢复 |
| M13 | `cuda-programming-optimization-interview-100` | kernel correctness、边界/竞争、性能实验 |
| M14 | `rl-interview-100-v2` | Bellman/GAE、环境 API、种子/置信区间 |
| M15 | `embodied-ai-interview-100` | 坐标/单位、sim2real、感知/规划指标 |
| M16 | `memcached-interview-100` | TTL、并发、逐出语义与源码版本 |
| M17 | `python-interview-100` | Python 版本、并发语义、可执行例子 |
| M18 | `operating-system-interview-100` | 调度/内存/同步语义、Linux 版本 |
| M19 | `sqlite-interview-100` | WAL、事务隔离、索引、SQL 反例 |
| M20 | `redis-interview-100-offer-style-v2` | 持久化、复制、集群和缓存一致性 |
| M21 | `Data-Structures-Interview-100` | 不变量、复杂度、随机化操作测试 |
| M22 | `computer-organization-interview-100` | Cache、流水线、TLB、一致性模型 |
| M23 | `computer-network-interview-100` | TCP/TLS/HTTP、抓包与故障复现 |
| M24 | `time-series-interview-100` | 数据泄漏、滚动验证、置信区间 |
| M25 | `crawler-anti-crawler-interview-100` | 抓取礼仪、限速、健壮性与数据合规 |
| M26 | `network-security-interview-100` | 威胁模型、授权边界、证据正确性 |
| M27 | `web-security-interview-100` | OWASP 风险、认证授权、防护测试 |
| M28 | `jianzhi-web3-offer-100` | EVM/合约语义、漏洞防护和版本 |
| M29 | `JianZhi-Quant-Offer` | 回测偏差、交易成本、样本外评测 |
| M30 | `microeconomics-interview-100` | 经济模型假设、图示/公式、反事实 |
| M31 | `macroeconomics-interview-100` | IS-LM/增长/货币模型口径与边界 |
| M32 | `control-theory-interview-100-v1.1.0` | 稳定性、离散化、仿真数值一致性 |
| M33 | `junior-math-competition-teacher-interview-100` | 题解严谨性、学生常见误解 |
| M34 | `high-school-math-olympiad-coach-interview` | 定理适用条件、完整证明、反例 |
| M35 | `game-engine-interview-100` | C++ 生命周期、性能数据、图形 API |

## 跨模块 P0（独立 PR，不混入 M01 内容更改）

根 README 的 `python3 site/build.py` 无法按当前 `main` Git 树直接复现：
`site/` 不存在于 Git 树且被根 `.gitignore` 忽略。

建议后续**独立**改为可跟踪的 `tools/site_builder/` 或 `scripts/site_build.py`，
使输入、构建命令和输出目录分离，配套集成测试与 GitHub Pages 发布工作流。
`can-interview-offer` 当前是未上线内容，单独设立“补题与验收”任务，不计入现有 35 套。
