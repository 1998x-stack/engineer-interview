# Recommender Systems Interview 100 · 2026

> 面向推荐算法 / 搜推算法 / 广告算法岗位的系统化面试知识库。

本仓库将《推荐系统面试 100 题》专业版 PDF 拆解为 **100 个独立 Markdown**，并升级为 **V2 深度版**：每题不仅保留“30 秒回答 / 深入拆解 / 公式”，还增加第一性原理、90 秒标准回答、数量级案例、工程决策矩阵、上线监控、边界条件、Senior/Staff 加分点，以及 **5 个连续追问 + 5 个参考答案**。

## 核心特性

- **100 题 = 100 个 Markdown**：便于搜索、复习、PR 修改与长期维护。
- **9 大章节**：完整覆盖召回、精排、序列、多任务、实验、偏差、冷启动与生成式推荐。
- **双层回答**：每题同时提供 30 秒快速回答和 90 秒可脱稿的完整回答。
- **500 个追问答案**：100 题 × 5 层追问，不再只有“问题列表”，而是给出可复述的参考答案。
- **工程决策导向**：每题都有数量级案例、Pareto 权衡、上线验证、监控字段、失败边界与回滚思路。
- **2026 前沿**：HSTU、Generative Recommendation、Semantic ID/RQ-VAE、RankMixer、LLM4Rec。
- **文档站可发布**：内置 MkDocs Material + GitHub Pages workflow。
- **可运行示例**：包含 ItemCF、Two-Tower InfoNCE、FM、指标、A/B 分桶、IPS、MMR 等最小实现。

## V2 单题结构

每个问题都按同一套面试训练协议组织：

1. **30 秒回答**：先建立一句话结论；
2. **深入拆解 + 数学机制**：理解为什么成立，而不是背模型名；
3. **V2 第一性原理**：把问题放回数据、模型、系统、指标四层；
4. **90 秒标准回答**：训练真实面试表达；
5. **数量级案例**：用候选数、维度、延迟、样本量把方案约束到工业尺度；
6. **工程决策矩阵**：明确 quality / latency / memory / stability 的权衡；
7. **上线验证与监控**：说明 offline → shadow → canary → A/B 的证据链；
8. **边界条件与失败案例**：主动回答“什么时候不该用”；
9. **5 个连续追问 + 参考答案**：模拟面试官逐层拷打；
10. **相关题与原始资料**：把单题连接回完整推荐知识图。

核心原始论文索引见 [`docs/references/primary-sources.md`](docs/references/primary-sources.md)。

## 仓库架构

完整目录与设计原则见 [REPO_STRUCTURE.md](REPO_STRUCTURE.md)。

## 推荐阅读顺序

1. 先看 [知识地图](docs/guide/knowledge-map.md)。
2. 用 [高频 20 题](docs/study/high-frequency-20.md) 建立主线。
3. 按 9 章逐题阅读：第一遍只看“30 秒回答”；第二遍练“90 秒标准回答”；第三遍专攻公式、工程决策矩阵与边界条件；最后遮住答案做 5 个连续追问。
4. 面试前使用 [项目拷打模板](docs/study/project-grilling-template.md) 复盘自己的项目。
5. 时间紧张时按 [7 天 / 30 天路线](docs/study/roadmap.md) 冲刺。

## 目录

| 章节 | 题号 | 主题 |
|---|---:|---|
| 1 | 001-010 | 系统架构与业务理解 |
| 2 | 011-025 | 召回、Embedding、双塔与负采样 |
| 3 | 026-038 | CTR 精排与特征交叉 |
| 4 | 039-050 | 用户行为序列与长兴趣建模 |
| 5 | 051-062 | 多任务、多目标与 CVR 建模 |
| 6 | 063-075 | Loss、排序指标与在线实验 |
| 7 | 076-085 | 偏差、数据、训练与在线工程 |
| 8 | 086-093 | 冷启动、多样性、长尾与探索 |
| 9 | 094-100 | HSTU、RankMixer、LLM 与生成式推荐 |

## 本地预览文档站

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 内容边界

- “面经高频”表示在公开面经中直接或高度同义出现，不代表公司官方题库。
- “论文追问”表示由经典模型定义自然展开的高频追问。
- “系统设计”表示根据工业推荐链路归纳出的高概率开放题。
- 本仓库聚焦推荐系统，不覆盖 LeetCode、概率统计或通用机器学习八股。

## PDF

原始专业版 PDF 保存在 [`docs/assets/recommender_system_interview_100_pro.pdf`](docs/assets/recommender_system_interview_100_pro.pdf)。
