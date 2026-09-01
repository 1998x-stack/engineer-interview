# 第 9 章 · 推理、分布式与 AI Infra

> **章节目标**：能从资源账本解释 LLM Serving/Training 优化：FLOPs、HBM、KV、通信与调度。

## 1. 先修知识

Transformer、GPU 基础、分布式 collective 概念。

## 2. 本章知识路线

Q091–Q095 Serving → Q096 Training/Distributed。

## 3. 必须白板掌握

- KV Cache state machine
- KV bytes 估算
- Quantization bandwidth
- Continuous Batching
- PagedAttention
- Speculative Decoding
- DP/TP/PP/EP communication

## 4. 高频失分模式

- KV cache 缓存 QKV
- INT4 文件小=一定快
- PagedAttention 减少数学 KV
- Speculative 是近似分布
- 并行度越大越快

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q091 | [KV Cache 为什么能显著加速自回归 Decode？](Q091-kv-cache.md) | ★★★★ | ★★★★★ |
| Q092 | [KV Cache 大小怎么估算？](Q092-kv-cache-memory.md) | ★★★★ | ★★★★★ |
| Q093 | [Quantization 为什么能提升 LLM 推理吞吐？](Q093-quantization.md) | ★★★★ | ★★★★ |
| Q094 | [Continuous Batching 与 PagedAttention 解决什么？](Q094-continuous-batching-pagedattention.md) | ★★★★ | ★★★★★ |
| Q095 | [Speculative Decoding 为什么能“保证分布”又加速？](Q095-speculative-decoding.md) | ★★★★★ | ★★★★ |
| Q096 | [DP、TP、PP、EP：四种并行怎么组合？](Q096-distributed-parallelism.md) | ★★★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
