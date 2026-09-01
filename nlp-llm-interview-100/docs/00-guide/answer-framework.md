# 专业面试回答框架

这套框架用于把“我知道这个概念”升级成“我能在高级算法面试中稳定讲清楚”。不是每道题都机械讲完 8 步，而是根据面试官追问深度逐层展开。

---

## 1. Definition：先定义边界

回答：

- 它是什么？
- 输入是什么？
- 输出是什么？
- 它属于训练、推理、检索还是数据处理哪个阶段？

避免：

> “它就是一种优化方法 / 一种位置编码 / 一种检索算法。”

更好：

> “GQA 保留多个 Query Heads，但让多个 Q Heads 共享一组 K/V Heads，核心目标是降低 Decode 阶段 KV Cache 和 HBM 读带宽。”

---

## 2. Objective / Formula：把结论落到数学对象

优先写：

- 概率分布；
- loss；
- score；
- state transition；
- tensor shape；
- 系统资源公式。

比如 Q092 不只说“KV Cache 很大”，要能写：

$$
2\times L\times T\times H_{kv}\times D_h\times \text{bytes}
$$

---

## 3. Why：回答“为什么这个设计有效”

最好的 Why 通常来自以下四类：

1. **统计假设**：CE 来自 categorical MLE；
2. **优化几何**：Pre-LN 提供更直接 residual gradient path；
3. **表示能力**：Multi-Head 提供多套 attention distribution；
4. **系统瓶颈**：GQA 为 Decode KV bandwidth 服务。

如果只能说“论文实验发现更好”，通常还不够深入。

---

## 4. Trade-off：不要只讲优点

至少从一个维度说明代价：

- Accuracy / Recall / Quality；
- FLOPs；
- Memory；
- HBM bandwidth；
- Latency；
- Communication；
- Data coverage；
- Bias / Calibration；
- Engineering complexity。

例：

> “MQA 比 GQA 更省 KV，但共享一组 K/V 可能损失表示容量；GQA 用更多 KV Heads 换取质量。”

---

## 5. Failure Modes：高阶回答的分水岭

问自己：

- 数据分布变了会怎样？
- 序列更长会怎样？
- 类别更不平衡会怎样？
- 低精度会怎样？
- 多机通信会怎样？
- 标注/Reward/Judge 有噪声会怎样？

高级候选人的特点不是“什么都说好”，而是知道设计什么时候会坏。

---

## 6. Implementation：能不能真的写出来

模型题优先写 shape：

```text
X       [B, T, d]
Q/K/V   [B, H, T, Dh]
Score   [B, H, Tq, Tk]
Output  [B, T, d]
```

算法题写复杂度：

```text
Exact Scan: O(Nd)
HNSW: approximate graph search
IVF: search only nprobe lists
```

系统题写资源：

```text
Compute
Memory
Bandwidth
Communication
Scheduler
```

---

## 7. Verification：如何证明实现正确

这是很多面试回答缺失的一层。

### 数学算法

- 小输入手算；
- brute-force reference；
- numerical gradient check。

### Transformer

- naive vs fused output / gradient 对拍；
- cached decode vs full forward logits 对拍；
- mask 可视化；
- shape / dtype asserts。

### RAG

- gold evidence Recall@K；
- rerank NDCG；
- answer faithfulness / correctness 分开；
- error attribution。

### 数据系统

- retention / reason code；
- false positive / false negative 抽样；
- proxy training ablation。

---

## 8. Production：连接线上系统

如果题目来自高级算法 / Research Engineer / Infra 岗，最后通常要落到：

- 监控什么？
- 怎样灰度？
- 怎样回滚？
- 线上分布漂移怎么办？
- 成本如何估？
- 单点故障在哪里？

---

## 9. 60 秒回答模板

可以使用：

> **定义**：X 是……  
> **机制**：核心公式 / 流程是……  
> **Why**：它主要解决……  
> **Trade-off**：代价是……

不要在第一分钟主动展开全部历史、论文和工程细节；给面试官留下继续追问的接口。

---

## 10. 3 分钟回答模板

```text
1. 一句话定义
2. 一个核心公式 / shape
3. 为什么有效
4. 对比上一种方法
5. 一个 trade-off
6. 一个失败模式
7. 一个实现 / 验证点
```

做到这一层，绝大多数八股题已经能转化成高级算法讨论。
