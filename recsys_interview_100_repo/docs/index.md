# Recommender Systems Interview 100 · 2026

> 面向推荐算法 / 搜推算法 / 广告算法岗位的系统化面试知识库。

本仓库将《推荐系统面试 100 题》专业版 PDF 拆解为 **100 个独立 Markdown**，并在原有“30 秒回答 / 深入拆解 / 公式 / 常见失分 / 连续追问”基础上补充工业级工程视角、回答框架、评分标准、交叉链接与参考论文。

## 核心特性

- **100 题 = 100 个 Markdown**：便于搜索、复习、PR 修改与长期维护。
- **9 大章节**：完整覆盖召回、精排、序列、多任务、实验、偏差、冷启动与生成式推荐。
- **面试导向**：每题都有 30 秒回答、深度原理、工程检查清单、失分点、追问树。
- **2026 前沿**：HSTU、Generative Recommendation、Semantic ID/RQ-VAE、RankMixer、LLM4Rec。
- **文档站可发布**：内置 MkDocs Material + GitHub Pages workflow。
- **可运行示例**：包含 ItemCF、Two-Tower InfoNCE、FM、指标、A/B 分桶、IPS、MMR 等最小实现。

## 推荐阅读顺序

1. 先看 [知识地图](guide/knowledge-map.md)。
2. 用 [高频 20 题](study/high-frequency-20.md) 建立主线。
3. 按 9 章逐题阅读；第一遍只看“30 秒回答”，第二遍看公式与工程，第三遍只看追问自测。
4. 面试前使用 [项目拷打模板](study/project-grilling-template.md) 复盘自己的项目。
5. 时间紧张时按 [7 天 / 30 天路线](study/roadmap.md) 冲刺。

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

原始专业版 PDF 保存在 [`assets/recommender_system_interview_100_pro.pdf`](assets/recommender_system_interview_100_pro.pdf)。
