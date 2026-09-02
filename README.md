# ∫ Engineer Interview 100 · 工程师面试系列知识库

> **16 大方向的体系化面试手册 · 1,600+ 道高频面试题 · 每题一个 Markdown · 每套配套 PDF**
> 覆盖 **算法 / 深度学习 / Transformer / 计算机视觉 / NLP·LLM / LLM 预训练 / LLM 后训练 / LLM 推理 / Agent / 推荐系统 / 搜索引擎 / Memcached / 强化学习 / 具身智能 / 金融量化 / 游戏引擎**。

[![Collections](https://img.shields.io/badge/collections-16-0fb9b1)](#📁-仓库结构与目录)
[![Questions](https://img.shields.io/badge/questions-1,600%2B-ff5f1f)](#📁-仓库结构与目录)
[![PDF Handbooks](https://img.shields.io/badge/PDF%20handbooks-16-red)](#🖨-可打印-pdf-手册)
[![Website](https://img.shields.io/badge/live%20preview-%E2%86%97-12263a)](https://1998x-stack.github.io/engineer-interview/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 🔗 **立即在线阅读 (GitHub Pages)** → **https://1998x-stack.github.io/engineer-interview/**
> 16 个教程概览 · 1,600+ 道题 · 站内题面解答 · LaTeX 公式 · 每套 PDF 在线阅读

> **让候选人成功并不难；真正的工程能力，是让答案「可控地失败」——先给结论，再给推导，再给工程决策与失败边界。**

本仓库把主流 **工程师 / 算法岗**的高频面试知识沉淀为 **16 个独立教程**，每个教程围绕一个方向组织出 **100 道核心题**，每题一 Markdown，并给出**可复述、可推导、可落地的参考答案**——而不是一张问题目录。

核心方法论贯穿所有教程：

> **Know-What → Know-Why → Know-How → Trade-off → Production**

---

## 🌐 在线站点 · GitHub Pages

全站已构建为一套可浏览的静态网站（16 个教程概览 → 教程详情 → 每道题的完整解答 + 站内 PDF 阅读器）：

🔗 **https://1998x-stack.github.io/engineer-interview/**

- **Overview**：16 个教程按意图分组，附「1600+ 题按规模可视化」的 scale-bar
- **教程页**：章节 → 100 道题阶梯 + 必刷题标记 + **站内 PDF 手册预览 / 下载**
- **题目页**：30s 回答 / 深度拆解 / 公式 / 边界条件 / 追问，含**在线 LaTeX 公式渲染**（MathJax）

---

## 目录

- [背景与定位](#背景与定位)
- [核心特性](#核心特性)
- [仓库结构与目录](#仓库结构与目录)
- [快速开始](#快速开始)
- [构建在线站点](#构建在线站点)
- [推荐学习路径](#推荐学习路径)
- [内容边界](#内容边界)
- [致谢与贡献](#致谢与贡献)
- [许可证](#许可证)

---

## 背景与定位

本仓库将主流工程师 / 算法岗位的高频面试知识，沉淀为 **16 个独立教程**，每个教程围绕一个方向整理 100 道核心题，覆盖从理论基础到生产系统的完整链路。

它面向：

- **准备社招 / 校招面试**的算法工程师、MLE、LLM / 基础模型、推荐 / 搜索 / 广告 / 引擎程序员等岗位候选人；
- 希望在 **Agent、LLM、Transformer、推荐系统、NLP、图形 / 渲染** 等方向系统补齐「理论 → 工程」闭环的工程师；
- 需要**结构化题库 + 学习路线 + 面试评分 Rubric** 的团队与个人成长资料库。

每个教程自带：**知识地图 / 章节索引 / 学习路线 / 必背书单 / 面试评分模板 / 配套 PDF**，可独立成册使用。

## 核心特性

- **一题一 Markdown**：每题独立成文，便于搜索、复习、PR 修改与长期维护。
- **多层答题协议**：每题提供「30 秒快速回答」+「90 秒可脱稿完整回答」+「数学机制 + 工程决策矩阵 + 上线验证 + 边界条件 + 连续追问」。
- **纵深覆盖**：从数据、模型、训练到推理、系统设计与生产工程，逐层打通。
- **可运行示例**：部分方向内置最小可运行代码（推荐 ItemCF / Two-Tower / FM / A/B；算法含完整 Python 题解与测试；Transformer 含参考实现）。
- **可打印 PDF**：每个教程都附带整本 PDF 手册。
- **在线阅读**：全站统一构建为 GitHub Pages 静态站，题库 + PDF + LaTeX 公式一站式浏览。

---
## 📁 仓库结构与目录

### 核心基础

| 教程 | 方向 | 核心内容 |
|---|---|---|
| [`algorithm-interview-100`](algorithm-interview-100/) | 算法 / LeetCode | 100 道母题 + 25+ 模式 + 工程化追问 + 题解与测试 |
| [`deep-learning-interview-100`](deep-learning-interview-100/) | 深度学习 | 结构、训练、正则化、序列建模、多模态、分布式与推理 |
| [`transformer-interview-100`](transformer-interview-100/) | Transformer | Attention、位置编码、LayerNorm、训练稳定、推理与系统设计 |
| [`nlp-llm-interview-100`](nlp-llm-interview-100/) | NLP / LLM | 序列建模、预训练、对齐、RAG、数据评估、推理与工程调试 |
| [`cv-algorithm-interview-handbook-v2`](cv-algorithm-interview-handbook-v2/) | 计算机视觉 | 检测、分割、OCR、视觉基础模型、生成式、视频与 3D 多模态 |

### LLM 全生命周期

| 教程 | 方向 | 核心内容 |
|---|---|---|
| [`llm-pretraining-interview-100`](llm-pretraining-interview-100/) | LLM 预训练 | Data、Scaling、分词、分布式训练、MoE、长上下文与训练稳定 |
| [`llm-post-training-offer`](llm-post-training-offer/) | LLM 后训练 | SFT / RLHF / DPO / GRPO、Reward、Verifier、RL 系统与 Agentic RL |
| [`llm-inference-interview-100-pro`](llm-inference-interview-100-pro/) | LLM 推理与部署 | KV Cache、量化、Batching、推测解码、MoE 与生产推理系统 |
| [`agent-engineer-interview-100`](agent-engineer-interview-100/) | Agent 工程 | Agent Loop、Multi-Agent、Tools/MCP、RAG、Durable Execution、Eval、Security |

### 应用系统与推荐

| 教程 | 方向 | 核心内容 |
|---|---|---|
| [`recsys_interview_100_repo`](recsys_interview_100_repo/) | 推荐系统 | 召回、双塔、精排、序列、多任务、实验、偏差、冷启动、生成式推荐 |
| [`search-engine-interview-100`](search-engine-interview-100/) | 搜索引擎 | 倒排索引、BM25、LTR、ANN、混合检索/RAG、搜索系统设计 |
| [`memcached-interview-100`](memcached-interview-100/) | Memcached / 缓存 | 源码穿透：slab、hashtable、LRU/TTL、线程模型、一致性、高可用 |

### AI 前沿

| 教程 | 方向 | 核心内容 |
|---|---|---|
| [`rl-interview-100-v2`](rl-interview-100-v2/) | 强化学习 | MDP、DQN / PPO、连续控制、离线 RL、RL 对齐与系统设计 |
| [`embodied-ai-interview-100`](embodied-ai-interview-100/) | 具身智能 | 感知、SLAM、规划、模仿学习、Sim2Real、VLM / VLA、World Model |

### 工程与金融

| 教程 | 方向 | 核心内容 |
|---|---|---|
| [`game-engine-interview-100`](game-engine-interview-100/) | 游戏引擎 / 图形 | C++ 对象模型、渲染管线、内存、数学、性能与引擎架构 |
| [`JianZhi-Quant-Offer`](JianZhi-Quant-Offer/) | 金融量化 | 因子、回测、风控、Alpha、市场微观结构、高频交易 |

> 📊 共 **16 教程 · 约 1,600+ 道题 · 16 本 PDF 手册**。

---

## 📌 快速开始

```bash
git clone git@github.com:1998x-stack/engineer-interview.git
cd engineer-interview
```

**按方向在线阅读**：进入任一教程的 `README.md`（或以本地 MkDocs 预览某个子教程）：

```bash
cd deep-learning-interview-100
python -m pip install -r requirements-docs.txt
mkdocs serve        # 预览单个教程的文档站
```

---

## 构建在线站点

整套教程可一键生成为统一静态站（`site/`），支持本地 `file://` 直接打开，或发布到 GitHub Pages：

```bash
python3 site/build.py            # 重新生成（解析全部 frontmatter 与题面）
cd site && python3 -m http.server 8000   # 本地预览 → http://localhost:8000
```

构建输出包含：**概览页 / 16 个教程页 / 1,600+ 题面页 / 所有 PDF 副本 / LaTeX 公式渲染**。在线版见 👉 [查看在线站点](https://1998x-stack.github.io/engineer-interview/)。

---

## 🧭 推荐学习路径

1. **先选方向**：根据目标岗位进入对应教程，先看其「知识地图 / 总索引」建立全局图景。
2. **再建主线**：用各教程的「高频 20」或「必刷列表」建立主线，逐题阅读。
3. **三轮复习**：第一遍只看「30 秒回答」建立结论；第二遍练「90 秒完整回答」练习表达；第三遍专攻公式、工程决策矩阵与边界条件。
4. **模拟面试**：使用内置的面试评分 Rubric 与模拟面试模板自测。
5. **PDF 通读**：配合教程的整本 PDF 手册做离线 / 地铁复习。

---

## 内容边界

- 每题内容均从公开面经、经典论文与源码归纳整理，**非任何公司的官方题库**。
- 各教程聚焦特定方向；LeetCode 母题仅隶属于 `algorithm-interview-100`，不覆盖通用八股。
- 每题的具体参考 / 溯源，请进入对应教程的 `docs/`（如 `references/`）查看。

---

## 🤝 致谢与贡献

欢迎对任意教程提交改进：修正推导、补充边界条件、增加追问或示例。请先在对应目录阅读 `CONTRIBUTING.md`，遵循每题的结构规范提交 PR。

项目配套的**在线统一站点**由仓库内 `site/build.py` 自动生成——新增或更新题目后执行 `python3 site/build.py` 即可重新生成所有页面。

---

## 许可证

除特别注明外，本仓库整体遵循各教程自带的 License 文件（多数为 **MIT**）。具体授权以各教程目录内的 `LICENSE` / `LICENSE-NOTICE` 为准。