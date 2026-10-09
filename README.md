# ∫ Engineer Interview 100 · 工程师面试系列知识库

> **35 大方向的体系化面试手册 · 3,500+ 道高频面试题 · 每题一个 Markdown · 每套配套 PDF**
> 覆盖 **算法 / 深度学习 / Transformer / 计算机视觉 / NLP·LLM / LLM 预训练 / LLM 后训练 / LLM 推理 / Agent / Agent Harness / 推荐系统 / 搜索引擎 / Memcached / Redis / SQLite / 操作系统 / 计算机网络 / 计算机组成 / 数据结构 / Python / 网络安全 / Web 安全 / 爬虫对抗 / 强化学习 / 具身智能 / CUDA / 时间序列 / 控制论 / 金融量化 / Web3 / 微观经济 / 宏观经济 / 数学竞赛教练 / 游戏引擎**。

[![Collections](https://img.shields.io/badge/collections-35-0fb9b1)](#-仓库结构与目录)
[![Questions](https://img.shields.io/badge/questions-3%2C533-ff5f1f)](#-仓库结构与目录)
[![PDF Handbooks](https://img.shields.io/badge/PDF%20handbooks-35-red)](#-可打印-pdf-手册)
[![Website](https://img.shields.io/badge/live%20preview-%E2%86%97-12263a)](https://1998x-stack.github.io/engineer-interview/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 🔗 **立即在线阅读 (GitHub Pages)** → **https://1998x-stack.github.io/engineer-interview/**
> 35 个教程概览 · 3,500+ 道题 · 站内题面解答 · LaTeX 公式 · 每套 PDF 在线阅读

> **让候选人成功并不难；真正的工程能力，是让答案「可控地失败」——先给结论，再给推导，再给工程决策与失败边界。**

本仓库把主流 **工程师 / 算法岗**的高频面试知识沉淀为 **35 个独立教程**，每个教程围绕一个方向组织出 **100 道核心题**，每题一 Markdown，并给出**可复述、可推导、可落地的参考答案**——而不是一张问题目录。

核心方法论贯穿所有教程：

> **Know-What → Know-Why → Know-How → Trade-off → Production**

---

## 🌐 在线站点 · GitHub Pages

全站已构建为一套可浏览的静态网站（35 个教程概览 → 教程详情 → 每道题的完整解答 + 站内 PDF 阅读器）：

🔗 **https://1998x-stack.github.io/engineer-interview/**

- **Overview**：35 个教程按领域分组，附「3,533 题按规模可视化」的 scale-bar
- **教程页**：章节 → 100 道题阶梯 + 必刷题标记 + **站内 PDF 手册预览 / 下载**
- **题目页**：30s 回答 / 深度拆解 / 公式 / 边界条件 / 追问，含**在线 LaTeX 公式渲染**（MathJax）

---

## 目录

- [背景与定位](#背景与定位)
- [核心特性](#核心特性)
- [仓库结构与目录](#-仓库结构与目录)
- [快速开始](#快速开始)
- [构建在线站点](#构建在线站点)
- [推荐学习路径](#推荐学习路径)
- [内容边界](#内容边界)
- [进行中 / Roadmap](#-进行中--roadmap)
- [致谢与贡献](#-致谢与贡献)
- [许可证](#许可证)

---

## 背景与定位

本仓库将主流工程师 / 算法岗位的高频面试知识，沉淀为 **35 个独立教程**，每个教程围绕一个方向整理 100 道核心题，覆盖从理论基础到生产系统的完整链路。

它面向：

- **准备社招 / 校招面试**的算法工程师、MLE、LLM / 基础模型、推荐 / 搜索 / 广告 / 引擎程序员、后端 / 基础架构、安全、量化、嵌入式与教育岗候选人；
- 希望在 **Agent、LLM、Transformer、推荐系统、NLP、系统基础、图形 / 渲染** 等方向系统补齐「理论 → 工程」闭环的工程师；
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

> 共 **35 教程 · 3,533 道题 · 35 本 PDF 手册**。下表按领域分组，题量为 build.py 实测值。

### 核心基础

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`transformer-interview-100`](transformer-interview-100/) | Transformer 架构 | 110 | Attention、位置编码、LayerNorm、训练稳定、推理优化与系统设计。 |
| [`cv-algorithm-interview-handbook-v2`](cv-algorithm-interview-handbook-v2/) | 计算机视觉 | 100 | 检测、分割、OCR、视觉基础模型、生成式、视频与 3D 多模态。 |
| [`nlp-llm-interview-100`](nlp-llm-interview-100/) | NLP 与 LLM | 100 | 搜索 / RAG、序列建模、预训练、对齐、数据评估、推理服务与工程调试。 |
| [`agent-engineer-interview-100`](agent-engineer-interview-100/) | 智能体工程 | 100 | Agent Loop、Multi-Agent、Tools/MCP、Context、RAG、Durable Execution、Eval、Security。 |
| [`deep-learning-interview-100`](deep-learning-interview-100/) | 深度学习 | 100 | 结构、优化与归一化、序列建模、多模态、分布式训练与推理优化。 |
| [`algorithm-interview-100`](algorithm-interview-100/) | 算法 | 102 | 100 道母题 + 25+ 模式 + 工程化追问，含题解与测试。 |

### LLM 生命周期

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`llm-pretraining-interview-100`](llm-pretraining-interview-100/) | LLM 预训练 | 101 | Data、Scaling Law、Tokenizer、分布式训练、MoE、长上下文与训练稳定。 |
| [`llm-inference-interview-100-pro`](llm-inference-interview-100-pro/) | LLM 推理 | 101 | KV Cache、量化、Batching、推测解码、MoE 与生产级推理系统（Pro 版）。 |
| [`llm-post-training-offer`](llm-post-training-offer/) | LLM 后训练 | 100 | SFT 数据、Reward Model、PPO/DPO/GRPO、Verifier、RL 系统与 Agentic RL。 |

### 应用系统与推荐

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`search-engine-interview-100`](search-engine-interview-100/) | 搜索引擎 | 100 | 倒排索引、BM25、LTR、ANN、混合检索/RAG、搜索系统设计。 |
| [`recsys_interview_100_repo`](recsys_interview_100_repo/) | 推荐系统 | 101 | 召回、双塔、精排、序列、多任务、实验、偏差、冷启动、生成式推荐。 |

### AI 前沿

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`agent-harness-interview-100`](agent-harness-interview-100/) | Agent 工程 (Harness) | 101 | Agent 运行时、工具、状态、可观测性与生产 Agent 系统。 |
| [`cuda-programming-optimization-interview-100`](cuda-programming-optimization-interview-100/) | CUDA 编程优化 | 101 | CUDA/GPU Kernel、内存模型、优化、Profiler、LLM Inference 与 GPU Compiler。 |
| [`rl-interview-100-v2`](rl-interview-100-v2/) | 强化学习 | 100 | MDP、DQN / PPO、连续控制、离线 RL、RL 对齐与系统设计。 |
| [`embodied-ai-interview-100`](embodied-ai-interview-100/) | 具身智能 | 101 | 感知、SLAM、规划、模仿学习、Sim2Real、VLM / VLA、World Model。 |

### 系统基础设施

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`memcached-interview-100`](memcached-interview-100/) | Memcached / 缓存 | 100 | 源码穿透：slab、hashtable、LRU/TTL、线程模型、一致性、高可用。 |
| [`python-interview-100`](python-interview-100/) | Python | 101 | Python 3.14：语言机制、并发、GC、异步、性能与工程题解。 |
| [`operating-system-interview-100`](operating-system-interview-100/) | 操作系统 | 100 | 进程、线程、内存、调度、同步、文件系统与 Linux 工程化。 |
| [`sqlite-interview-100`](sqlite-interview-100/) | SQLite | 100 | 事务、WAL、B-Tree/Pager、Query Planner、索引与系统设计。 |
| [`redis-interview-100-offer-style-v2`](redis-interview-100-offer-style-v2/) | Redis | 101 | 数据结构、持久化、集群、复制、缓存一致性的 Offer 风格。 |
| [`Data-Structures-Interview-100`](Data-Structures-Interview-100/) | 数据结构 | 103 | 数组、链表、栈、队列、堆、树、哈希、并查集与进阶数据结构。 |

### 计算机基础

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`computer-organization-interview-100`](computer-organization-interview-100/) | 计算机组成 | 100 | 数据表示、ISA、流水线、乱序执行、Cache、MMU/TLB、多核一致性与性能分析。 |
| [`computer-network-interview-100`](computer-network-interview-100/) | 计算机网络 | 100 | TCP、HTTP、TLS、路由、NAT、Linux 网络栈与线上故障定位。 |

### 数据 / 数据工程

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`time-series-interview-100`](time-series-interview-100/) | 时间序列 | 100 | ARIMA、状态空间、DeepTS、TSFM 与时序工程。 |
| [`crawler-anti-crawler-interview-100`](crawler-anti-crawler-interview-100/) | 爬虫与反爬 | 100 | HTTP 语义、Scrapy、URL 调度、Bot 检测、限流与分布式。 |

### 网络安全

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`network-security-interview-100`](network-security-interview-100/) | 网络安全 | 100 | 加密、认证、防火墙、安全协议、渗透测试与 SOC 实践。 |
| [`web-security-interview-100`](web-security-interview-100/) | Web 安全 | 103 | 注入、认证、OAuth、CSRF、供应链与渗透测试。 |

### 加密 / 金融工程

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`jianzhi-web3-offer-100`](jianzhi-web3-offer-100/) | Web3 / Solidity | 101 | Solidity、EVM、Security、DeFi、L2、AA、Solana 与系统设计。 |
| [`JianZhi-Quant-Offer`](JianZhi-Quant-Offer/) | 金融量化 | 101 | 因子、回测、风控、Alpha、市场微观结构、高频交易。 |

### 经济 / 金融

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`microeconomics-interview-100`](microeconomics-interview-100/) | 微观经济学 | 103 | 供需、弹性、博弈、市场结构、契约与反事实建模。 |
| [`macroeconomics-interview-100`](macroeconomics-interview-100/) | 宏观经济学 | 102 | GDP、IS-LM、货币、通胀、增长与金融市场。 |

### 车载 / 嵌入式 / 控制

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`control-theory-interview-100-v1.1.0`](control-theory-interview-100-v1.1.0/) | 控制论 | 100 | 传递函数、状态空间、PID、稳定性、鲁棒控制与离散系统。 |

### 教育 / 学科竞赛

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`junior-math-competition-teacher-interview-100`](junior-math-competition-teacher-interview-100/) | 初中数学竞赛教师 | 100 | 代数、几何、数论、教学法与追问 Rubric。 |
| [`high-school-math-olympiad-coach-interview`](high-school-math-olympiad-coach-interview/) | 高中数学竞赛教练 | 100 | 数论、组合、代数、几何、教练法与强基。 |

### 图形与游戏引擎

| 教程 | 方向 | 题量 | 核心内容 |
|---|---|---:|---|
| [`game-engine-interview-100`](game-engine-interview-100/) | 游戏引擎 / 图形 | 100 | C++ 对象模型、渲染管线、内存、数学、性能与引擎架构。 |

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

构建输出包含：**概览页 / 35 个教程页 / 3,533 题面页 / 所有 PDF 副本 / LaTeX 公式渲染**。在线版见 👉 [查看在线站点](https://1998x-stack.github.io/engineer-interview/)。

> 说明：`site/` 为构建产物，已在 `.gitignore` 中忽略；线上发布走 `gh-pages` 分支。

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

## 🚧 进行中 / Roadmap

| 方向 | 状态 | 备注 |
|---|---|---|
| `can-interview-offer`（车载 CAN / AUTOSAR） | **未纳入站点** | 已有 10 章导读与 PDF 大纲，但 `questions/` 题源目录尚未落地；补齐 100 题题解后从 `site/build.py` 的 `SKIP_SLUGS` 中移除即可上线。 |

---

## 🤝 致谢与贡献

欢迎对任意教程提交改进：修正推导、补充边界条件、增加追问或示例。请先在对应目录阅读 `CONTRIBUTING.md`，遵循每题的结构规范提交 PR。

项目配套的**在线统一站点**由仓库内 `site/build.py` 自动生成——新增或更新题目后执行 `python3 site/build.py` 即可重新生成所有页面。

---

## 许可证

除特别注明外，本仓库整体遵循各教程自带的 License 文件（多数为 **MIT**）。具体授权以各教程目录内的 `LICENSE` / `LICENSE-NOTICE` 为准。
