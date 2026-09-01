# 剑指 LLM 后训练 Offer

> 100 道 LLM Post-Training 面试题 · 一题一 Markdown · 原理推导 · 工程实战 · Failure-Driven 学习路线

本仓库基于配套 PDF 扩展为可维护的 GitHub 知识库。目标不是背 100 个“标准答案”，而是形成：

```text
Problem -> Objective -> Data -> Reward -> Exploration -> Credit Assignment
        -> Compute/System -> Failure Mode -> Algorithm Choice -> Eval
```

## 为什么这个仓库和普通面经不同

- **100 题一题一文件**：每题都有稳定 URL，适合收藏、review、PR 与讨论。
- **区分来源与扩展**：PDF 原始提要与外部研究补充分开标识。
- **面试回答阶梯**：30 秒、2 分钟、5 分钟三种深度。
- **Know-Why + Know-How**：不仅“是什么”，还解释为什么、怎么实现、哪里会坏。
- **Failure-Driven**：用失败模式理解 PPO -> GRPO -> DAPO / GSPO 的演化。
- **工程可观测**：每题尽量落到日志、指标、吞吐、显存、staleness 与 ablation。
- **可直接发布文档站**：提供 MkDocs Material 配置和 CI 校验。

## 十章

- **第 1 章 · [后训练全景与 SFT](01-sft-data/README.md)** — 目标、数据质量、采样、CoT 冷启动与方法选择
- **第 2 章 · [Preference、Reward Model 与 Reward Design](02-reward-model/README.md)** — 偏好数据、BT 模型、Reward Hacking、Verifier
- **第 3 章 · [PPO / GAE / 经典 RLHF](03-ppo-gae/README.md)** — importance sampling、clip、critic、KL、GAE
- **第 4 章 · [DPO 与 Offline Preference Optimization](04-dpo-family/README.md)** — DPO 推导、offline shift、KTO/ORPO/SimPO
- **第 5 章 · [GRPO](05-grpo/README.md)** — group-relative baseline、token credit、off-policy 与 rollout
- **第 6 章 · [DAPO / GSPO](06-dapo-gspo/README.md)** — 长 CoT RL 的 failure modes、sequence-level optimization、MoE
- **第 7 章 · [Reasoning RL、Verifier 与 Credit Assignment](07-reasoning-verifier/README.md)** — 探索、可验证奖励、稀疏奖励、熵与 hacking
- **第 8 章 · [RL 系统、Rollout 与分布式训练](08-rl-systems/README.md)** — 数据流、吞吐、长尾、vLLM、FSDP/ZeRO、训推分离
- **第 9 章 · [训练稳定性、评测与 Debug](09-eval-debug/README.md)** — 曲线诊断、ablation、数据/算法/系统归因
- **第 10 章 · [Agentic RL 与系统设计](10-agentic-rl/README.md)** — 长程 MDP、tool calling、credit、reward、项目答辩

## 快速入口

- [100 题总索引](question-index.md)
- [十章知识地图](00-guide/knowledge-map.md)
- [核心白板公式](00-guide/core-formulas.md)
- [算法演化：Failure Mode -> Method](00-guide/algorithm-evolution.md)
- [高频 20 题](11-playbooks/top-20.md)
- [五条模拟面试路线](11-playbooks/mock-interview-routes.md)
- [项目终面研究决策链](11-playbooks/project-defense.md)
- [RL 系统 Debug 顺序](11-playbooks/rl-system-debug.md)
- [公开真题索引](12-appendix/real-interview-index.md)
- [14 天冲刺计划](12-appendix/14-day-plan.md)
- [论文与工程资料](12-appendix/references.md)

## 本地预览

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

然后访问终端输出的本地地址。

## 仓库质量检查

```bash
python scripts/validate_questions.py
python scripts/check_internal_links.py
mkdocs build --strict
```

## 推荐学习法

1. 先读 [使用指南](00-guide/README.md)。
2. 高频 20 题练到 5-10 分钟，其余题练到 60-90 秒。
3. 所有公式都要能解释符号对应哪个 tensor / policy version。
4. 所有“算法选择题”都从任务约束和 failure mode 出发。
5. 最终把抽象答案替换成你的项目数字与 ablation。

## 内容口径

公开面经是候选人自述，不代表企业官方题库。仓库会明确区分 PDF 来源、公开论文事实与工程性补充，详见 [内容口径与来源方法](12-appendix/source-methodology.md)。


## V2 专业版工具箱

- [研究方法论：从现象到可证伪实验](00-guide/research-methodology.md)
- [后训练工程实现检查表](00-guide/implementation-checklist.md)
- [白板训练：12 组必画图/必推公式](11-playbooks/whiteboard-drills.md)
- [实验设计 Playbook](11-playbooks/experiment-design.md)
- [Glossary](12-appendix/glossary.md)
