# 项目拷打模板

高质量推荐算法面试通常不是“模型八股结束”，而是围绕你的项目持续追问。建议把任何项目压缩成下面 7 层。

## 1. 背景与规模

- 业务目标是什么？
- 用户 / Item 数量级？DAU/MAU？QPS？
- 当前瓶颈是效果、延迟、覆盖率、冷启动还是成本？

## 2. Baseline

- 为什么选当前 baseline？
- 原系统最关键的 2-3 个缺点是什么？
- baseline 的离线与线上指标分别是多少？

## 3. 改动

分别说清：**数据、特征、模型、loss、采样、serving** 改了什么。不要把所有收益归因于“模型结构升级”。

## 4. 实验

- 离线：AUC/GAUC/NDCG/Recall@K，怎么 split？
- 在线：A/B 流量、周期、显著性、MDE、guardrail。
- 是否做了 cohort / user segment / scenario slice？

## 5. 归因

收益来自：更多数据？更好负样本？更多算力？更强模型？更好 serving freshness？需要 ablation 证明。

## 6. 失败实验

准备至少 2 个失败尝试：为什么当时看起来合理、为什么失败、如何定位、学到了什么。

## 7. 工程与风险

Latency、显存/内存、CPU/GPU、Feature freshness、灰度、故障回滚、监控、索引/模型版本一致性。
