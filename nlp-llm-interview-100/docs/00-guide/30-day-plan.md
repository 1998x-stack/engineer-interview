# 30 天刷题计划

目标不是 30 天“看完 100 题”，而是建立 **长期可提取的知识网络**。每天建议 60–120 分钟；若时间更少，优先完成“闭卷口述 + 一道白板推导”。

## 总体计划

| 天数 | 内容 | 核心产出 |
|---|---|---|
| 1–3 | Q001–Q012 | ML / 概率基础 60 秒回答 + 6 个核心公式 |
| 4–6 | Q013–Q024 | HMM/CRF/BM25/DP 的白板推导 |
| 7–9 | Q025–Q034 | Word2Vec→RNN→Attention 演进链 |
| 10–14 | Q035–Q050 | Transformer 全链路，重点 Shape/RoPE/GQA |
| 15–18 | Q051–Q064 | LM 目标、Tokenizer、Scaling、Data、Precision |
| 19–21 | Q065–Q074 | LoRA/QLoRA/RLHF/DPO/GRPO 对比 |
| 22–24 | Q075–Q084 | Retrieval/ANN/Rerank/RAG Eval |
| 25–26 | Q085–Q090 | 数据 Curation、Synthetic、Judge、线上 Gap |
| 27–28 | Q091–Q096 | KV Cache、Quant、Serving、Distributed |
| 29 | Q097–Q100 | Coding / Debug 闭卷实现 |
| 30 | 全随机模拟 | 20 题限时 + 错误簿收敛 |

---

## 每日固定动作

### 1. Retrieval Practice — 20 分钟

随机抽 5 道已学题：

- 每题 60 秒；
- 不看答案；
- 记录卡住位置。

### 2. Deep Work — 30–60 分钟

当天新题中选 2 道：

- 白板写公式 / shape；
- 读专业深挖；
- 回答追问树；
- 设计一个验证实验。

### 3. Error Log — 10 分钟

只记录：

- 错公式；
- 概念混淆；
- 没想到的 trade-off；
- 工程边界；
- 面试表达问题。

---

## 每周目标

### Week 1：基础不失分

必须能闭卷回答：

- CE vs MSE；
- AUC；
- BN vs LN；
- AdamW；
- HMM vs CRF；
- BM25；
- Negative Sampling；
- RNN 梯度；
- LSTM；
- Seq2Seq Attention。

### Week 2：Transformer 成为主战区

每天至少写一次：

$$
\mathrm{softmax}(QK^T/\sqrt{d_k})V
$$

并闭卷完成：

- `[B,T,d] → [B,H,T,Dh]`；
- causal mask；
- $R_m^TR_n=R_{n-m}$；
- Pre-LN；
- SwiGLU；
- GQA/KV Cache。

### Week 3：LLM 后训练 + RAG

目标是能连续讲 15 分钟：

```text
Pretraining
→ SFT
→ LoRA / QLoRA
→ Preference Data
→ DPO / PPO / GRPO
```

以及：

```text
BM25 + Dense
→ ANN
→ Rerank
→ Context Construction
→ RAG Evaluation
```

### Week 4：Data + Infra + Coding

重点不是背术语，而是做资源账本和测试设计：

- KV Cache bytes；
- HBM bandwidth；
- INT4/INT8；
- Continuous Batching；
- Speculative Decoding；
- DP/TP/PP/EP；
- Cached vs Full Forward consistency。

---

## Day 30 模拟规则

随机 20 题：

- 10 题：每题 60 秒；
- 6 题：每题 3 分钟；
- 2 题：白板推导；
- 2 题：Coding / System Design。

评分采用 0–5：

- 0：不知道；
- 1：只会定义；
- 2：会公式；
- 3：会 Why / trade-off；
- 4：会边界 / 实现；
- 5：会系统化 / 验证 / 追问。

**目标**：高频 ★★★★ / ★★★★★ 题平均 ≥4。
