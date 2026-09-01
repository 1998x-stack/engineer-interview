---
id: "Q033"
title: "Teacher Forcing 有什么问题？"
chapter: 4
chapter_name: "序列模型与语言模型基础"
difficulty: "★★☆"
frequency: "中频"
priority: "A"
pdf_page: 26
tags:
  - deep-learning
  - interview
  - sequence-model
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q033 · Teacher Forcing 有什么问题？

> **章节：** 序列模型与语言模型基础
> **难度：** ★★☆ ｜ **频度：** 中频 ｜ **优先级：** A
> **PDF 对应：** 第 26 页附近

## 面试官在考什么

考察训练/推理分布偏差。

**高质量回答标准：** 能区分训练与自回归推理；能正确处理 tokenization、mask、shift 等序列细节。

## 一句话结论

训练时 Teacher Forcing 把真实前一 token 作为下一步输入，而推理时只能使用模型自己的预测；一旦模型犯错，后续输入分布偏离训练分布并累积错误，这就是 exposure bias。

## 60–90 秒面试回答

训练时 Teacher Forcing 把真实前一 token 作为下一步输入，而推理时只能使用模型自己的预测；一旦模型犯错，后续输入分布偏离训练分布并累积错误，这就是 exposure bias。

## 深度解析

- Scheduled sampling 曾尝试逐步混入模型预测，但也有目标不一致问题。
- 自回归 Transformer 训练同样使用 ground-truth shifted tokens，因此也存在广义 exposure bias。
- 后训练、序列级目标和数据构造可以缓解但不是完全消除。



## 数学、Shape 与复杂度

建议至少写出一个最小数学表达或 shape 关系，并明确 reduction/statistics 发生在哪些维度；若属于经验型问题，则给出可验证的实验假设。

## 工程实现 / PyTorch 验证

### 推荐验证协议

比较 teacher-forced validation loss 与 free-running sequence quality；尝试 scheduled sampling 并观察副作用。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 序列任务首先明确 teacher forcing / autoregressive inference 的训练-推理差异。
- Tokenization、padding、mask 和 label shift 是最容易出现 silent bug 的四个位置。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 为什么语言模型训练可以并行而推理不能？
- sequence-level training 怎么做？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 把 exposure bias 误解为过拟合。

### 3 分钟展开框架

1. 先区分训练阶段与 autoregressive inference；
2. 再写 hidden/token 的状态转移或 mask；
3. 解释 tokenization / padding / shift 的细节；
4. 给出 exposure bias 或数据预处理错误的例子。

## 实战练习

- **可视化**：画一个长度不同的 batch，标出 padding mask、causal mask 和 labels。
- **代码**：检查 tokenizer 输出、EOS/BOS、label shift 是否一致。
- **故障注入**：故意不 mask padding，观察 loss/生成有什么变化。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

Teacher forcing 的 train/inference context distribution 不一致形成 exposure bias；误差在自回归 rollout 中会累积。

### 工程与实验抓手

比较 teacher-forced validation loss 与 free-running sequence quality；尝试 scheduled sampling 并观察副作用。

### 失败边界 / 反例

scheduled sampling 本身也可能引入不一致估计；现代 LLM 更多从数据、sequence-level objective 或 RL 角度处理。

### 白板专项练习

给出一个早期 token 预测错误导致后续条件分布完全改变的例子，解释 token-level loss 的局限。

> **本章 90 分标准：** 序列题要把训练信息流、推理信息流和 mask/tokenization 语义分开，不要只背架构名词。

## 面试官评分拆解

| 档位 | 典型表现 |
|---|---|
| 40–50 分 | 只会给定义或背结论，缺公式/机制，追问一层就断。 |
| 60–70 分 | 能解释主机制并写关键公式，但缺边界条件和工程证据。 |
| 80–90 分 | 能定量推导、比较替代方案，主动说明失败场景并给验证方法。 |
| 90+ 分 | 能把数学、实现、系统成本和项目决策串成完整证据链，并能反向设计实验验证假设。 |

### 面试表达建议

建议用 **结论 → 机制 → 定量 → trade-off → 边界 → 验证** 六步法回答。先在 60–90 秒内给主线；只有面试官继续追问时再展开公式、代码或系统细节。这样既显示深度，也避免一上来堆知识点失去重点。

## 项目化证据链：如何证明你真的做过

只讲原理只能证明“学过”，项目面试还要证明“做过、量过、复盘过”。针对本题，建议准备一张实验卡：**问题/假设 → baseline → 改动 → 指标 → 结果 → 失败 slice → 结论**。

### 建议报告的指标

- **核心观测：** token-level loss、sequence metric、长度分布、mask 正确率、free-running error、tokens/s。
- **证据原则：** 显式区分 training context 与 inference context，并做 token/mask 可视化审计。
- **本题特定证据：** 比较 teacher-forced validation loss 与 free-running sequence quality；尝试 scheduled sampling 并观察副作用。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**scheduled sampling 本身也可能引入不一致估计；现代 LLM 更多从数据、sequence-level objective 或 RL 角度处理。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先画 token/状态信息流 → 写 mask/目标 → 区分训练与推理 → 分析序列误差 → 给实现测试。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q032 · 为什么 LSTM 能缓解梯度消失？](../04-sequence-language-models/Q032-lstm-gradient.md)
- [Q034 · BERT 的预训练目标是什么？为什么它适合理解类任务？](../04-sequence-language-models/Q034-bert-pretraining.md)
- [Q031 · RNN、LSTM、GRU 的主要区别是什么？](../04-sequence-language-models/Q031-rnn-lstm-gru.md)
- [Q035 · Encoder-only、Decoder-only、Encoder-Decoder 如何选择？](../04-sequence-language-models/Q035-transformer-architectures.md)

## 参考资料

- [Devlin et al., BERT](https://arxiv.org/abs/1810.04805)
- [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
