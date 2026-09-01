# 30 天刷题路径 · 强化版

> 每天建议 90–150 分钟。原则：**少看答案，多做主动提取与实现。**

## Week 1 · Attention 基础成为肌肉记忆

### Day 1 · Q001–Q005
架构动机、Residual、Norm。

**产出**：画出 RNN vs Transformer 计算图；手推 residual Jacobian。

### Day 2 · Q006–Q010
Shape、参数、Self/Cross、Position。

**产出**：不运行代码写 `[B,T,D] → [B,H,T,Dh]`。

### Day 3 · Q011–Q015
Attention、scale、mask、softmax、多头。

**产出**：手算一个 3-token attention。

### Day 4 · Q016–Q020
head dim、QKV、complexity、causal。

**产出**：推 $O(Td^2+T^2d)$，扫描何时两项相等。

### Day 5 · Q021–Q025
padding、dropout、解释性、linear attention、sinusoidal。

**Coding**：reference attention + mask unit tests。

### Day 6 · 随机 20 题快答
每题 45 秒。

### Day 7 · Mock #1
包含 1 道 Attention coding。

## Week 2 · Position / Norm / BERT-GPT / Training

### Day 8–9 · Q026–Q034
RoPE 必须能从旋转矩阵推到相对位移。

### Day 10 · Q035–Q044
Pre-LN、RMSNorm、SwiGLU、初始化。

### Day 11–12 · Q045–Q054
BERT/GPT/encoder-decoder、MLM/CLM、teacher forcing。

### Day 13–14 · Q055–Q064
loss mask、NaN、AdamW、grad clip、BF16。

**Coding**：tiny overfit + finite hooks。

## Week 3 · Scaling / KV Cache / Serving

### Day 15 · Q065–Q067
Scaling law、多 GPU、生成循环。

### Day 16 · Q068–Q072
KV cache + GQA。

**必须手算**：至少 3 个 KV cache 配置。

### Day 17 · Q073–Q079
Decoding、latency、continuous batching、PagedAttention、speculative。

### Day 18 · Q080–Q084
FlashAttention、online softmax、sparse/linear。

### Day 19 · Q085–Q090
长上下文、MoE、quantization、MHA coding。

### Day 20–21 · Serving Mock
完成 SD02/SD03，做 concurrency sweep 设计。

## Week 4 · Coding / Debug / 综合

### Day 22 · Q091–Q093
读代码找数学 bug；建立 Debug checklist。

### Day 23 · Q094–Q099
未来泄漏、cache parity、stride、fully mask、tiny overfit、assertions。

### Day 24 · Q100 + SD01
文本分类 + 机器翻译设计。

### Day 25 · SD04–SD06
长上下文、70B 训练、Packing。

### Day 26 · SD07–SD10
现代架构、GPU、profiling、陌生变体。

### Day 27 · 30 题随机口试
错误题必须写入 mistakes log。

### Day 28 · Coding Mock
60 分钟：实现 Attention + 测试。

### Day 29 · System Mock
60 分钟：Serving / 70B / Long Context 三选一。

### Day 30 · Final Loop
只复习：

- 错题；
- 公式；
- 5 个手算；
- 5 个 Gotchas；
- 2 个 System Design。

## 每日 Definition of Done

- 5 道题脱稿回答；
- 2 道手推；
- 1 个代码/单测；
- 1 个性能或数值实验；
- 3 个错因记录。

## 评分

每题 0–4：

- 0：不会；
- 1：知道定义；
- 2：会公式；
- 3：能讲 trade-off / Gotcha；
- 4：能验证 + 迁移到陌生变体。

最终目标不是 100 个 2 分，而是高频核心题达到 4 分。
