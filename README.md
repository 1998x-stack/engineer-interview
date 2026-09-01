# Engineer Interview 100 · 工程师面试系列知识库

> **从算法、深度学习到 LLM 全链路面试题的体系化手册 · 9 大方向 · 900+ 道高频面试题**
> 覆盖 **算法 / 推荐系统 / 深度学习 / Transformer / NLP·LLM / LLM 预训练 / LLM 后训练 / Memcached / Agent** 等方向，
> 每题一 Markdown，强调 **Know-What → Know-Why → Know-How → Trade-off → Production** 五层答题法。

[![Collections](https://img.shields.io/badge/collections-9-blue)](#📁-仓库结构与目录)
[![Questions](https://img.shields.io/badge/questions-900%2B-brightgreen)](#📁-仓库结构与目录)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-MkDocs%20Material-8A2BE2)](#)

---

## 目录

- [背景与定位](#背景与定位)
- [核心特性](#核心特性)
- [仓库结构与目录](#仓库结构与目录)
- [快速开始](#快速开始)
- [推荐学习路径](#推荐学习路径)
- [内容边界](#内容边界)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 背景与定位

本仓库将 **主流工程师 / 算法岗位的高频面试知识** 沉淀为 **9 个独立的作品集子仓库**，每个子仓库围绕一个方向整理出 100 道核心问题，并给出**可复述、可推导、可落地的参考答案**，而不是一张“问题目录”。

它面向：

- **准备社招 / 校招面试**的算法工程师、MLE、LLM / 基础模型、推荐 / 搜索 / 广告算法岗位候选人；
- 希望在 **Agent、LLM 预训练 / 后训练、Transformer、推荐系统、NLP** 等方向系统补齐理论到工程闭环的工程师；
- 需要**结构化题库 + 学习路线 + 面试评分 Rubric** 的团队与个人成长资料库。

核心方法论贯穿所有子仓库：

> **让候选人成功并不难；真正的工程能力，是让答案**可控地失败**——先给结论，再给推导，再给工程决策与失败边界。**

## 核心特性

- **一题一 Markdown**：每题独立成文，便于搜索、复习、PR 修改与长期维护。
- **双层 / 多层答题协议**：每题提供「30 秒快速回答」+「90 秒可脱稿完整回答」+「数学机制 + 工程决策矩阵 + 上线验证 + 边界条件 + 连续追问」。
- **纵深覆盖**：从冷启动、召回 / 精排、归一化到模型训练、后训练、推理系统与 Agent 可靠性。
- **可运行示例**：部分方向内置最小可运行代码（如推荐系统的 ItemCF、Two-Tower、A/B 分桶）。
- **文档站可发布**：内置 MkDocs Material + GitHub Pages workflow，可一键本地预览 / 部署。
- **可打印 PDF**：部分方向附带整本 PDF 手册与 7 / 30 天学习路线。

## 仓库结构与目录

| 子仓库 | 方向 | 核心内容 |
|---:|---|---|
| [`agent-engineer-interview-100`](agent-engineer-interview-100/) | Agent Engineer | Agent Loop、Multi-Agent、Context、RAG、Durable Execution、Eval、Security、Production System Design |
| [`algorithm-interview-100`](algorithm-interview-100/) | 算法 / LeetCode | 100 道母题 + 25+ 模式 + 工程化追问 |
| [`deep-learning-interview-100`](deep-learning-interview-100/) | 深度学习 | 网络结构、训练、正则化、多模态、部署 |
| [`llm-post-training-offer`](llm-post-training-offer/) | LLM 后训练 | SFT / RLHF / DPO、对齐、偏好优化、评估、Failure-Driven 学习 |
| [`llm-pretraining-interview-100`](llm-pretraining-interview-100/) | LLM 预训练 | Data、Scaling、Tokenization、并行、Loss、训练稳定与生产化 |
| [`memcached-interview-100`](memcached-interview-100/) | Memcached / 缓存 | 源码穿透版：内存、淘汰策略、协议、线程模型、高可用 |
| [`nlp-llm-interview-100`](nlp-llm-interview-100/) | NLP / LLM | 搜索 / RAG、质量模型训练、后训练、数据工程与 AI Infra |
| [`recsys_interview_100_repo`](recsys_interview_100_repo/) | 推荐系统 | 召回、双塔、精排、序列、多任务、实验、偏差、冷启动 |
| [`transformer-interview-100`](transformer-interview-100/) | Transformer | Attention、位置编码、LayerNorm、训练、推理优化 |

## 📌 快速开始

克隆本仓库：

```bash
git clone git@github.com:<YOUR_USER>/engineer-interview.git
cd engineer-interview
```

按方向进入子仓库，阅读其 `README.md` 获取速览；或直接：

```bash
# 进入任一子仓库，本地预览文档站（若该子仓库内置 MkDocs）
cd deep-learning-interview-100
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 🧭 推荐学习路径

1. **先选方向**：根据目标岗位进入相应的子仓库，先看其「知识地图 / 总索引」建立全局图景。
2. **再建主线**：用各子仓库的「高频 100」或「必刷 20」建立主线，逐题阅读。
3. **三轮复习**：第一遍只看「30 秒回答」建立结论；第二遍练「90 秒完整回答」练习表达；第三遍专攻公式、工程决策矩阵与边界条件。
4. **模拟面试**：使用内置的面试评分 Rubric 与模拟面试模板进行自测。

## 内容边界

- 每道题内容均从公开面经与经典论文 / 源码归纳整理，非任何公司的官方题库。
- 各子仓库聚焦特定方向，不覆盖 LeetCode 之外的通用八股（LeetCode 隶属于 `algorithm-interview-100`）。
- 具体参考与原始论文索引，请进入对应子仓库的 `docs/` 查看。

## 🤝 贡献指南

欢迎对任意子仓库提交改进：修正推导、补充边界条件、增加追问或案例。请先在对应子目录阅读其 `CONTRIBUTING.md`，并遵循每题的结构规范提交 PR。

## License

除特别注明外，本仓库整体遵循各子仓库自带的 License 文件（多数为 MIT）。具体授权以各子仓库内的 `LICENSE` 为准。