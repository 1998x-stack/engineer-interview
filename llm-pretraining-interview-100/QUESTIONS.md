# 100 题总索引

> 可按浏览器搜索题号、关键词、难度或题型。

| ID | 题目 | 章节 | 类型 | 频率 | 难度 |
|---|---|---|---|---|---|
| Q001 | [手推 Self-Attention：为什么要除以 √d_k？](./questions/01-transformer-architecture/001.md) | Transformer 与模型架构 | A 类高频真题型 | ★★★★★ | 中 |
| Q002 | [MHA、MQA、GQA 的本质区别是什么？](./questions/01-transformer-architecture/002.md) | Transformer 与模型架构 | A 类高频真题型 | ★★★★★ | 中 |
| Q003 | [为什么大模型主流选择 Decoder-only？](./questions/01-transformer-architecture/003.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★★☆ | 中 |
| Q004 | [Pre-Norm 与 Post-Norm：为什么超深模型常用 Pre-Norm？](./questions/01-transformer-architecture/004.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★★☆ | 中 |
| Q005 | [RMSNorm 与 LayerNorm 的区别是什么？](./questions/01-transformer-architecture/005.md) | Transformer 与模型架构 | A 类高频真题型 | ★★★★★ | 易 |
| Q006 | [SwiGLU 为什么替代传统 ReLU/GELU FFN？](./questions/01-transformer-architecture/006.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★★☆ | 中 |
| Q007 | [RoPE 为什么能把相对位置信息写进 Attention？](./questions/01-transformer-architecture/007.md) | Transformer 与模型架构 | A 类高频真题型 | ★★★★★ | 难 |
| Q008 | [为什么现代 LLM 很少使用原始绝对位置 Embedding？](./questions/01-transformer-architecture/008.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★☆☆ | 中 |
| Q009 | [Embedding 与 LM Head 为什么要 Weight Tying？什么时候不 Tying？](./questions/01-transformer-architecture/009.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★☆☆ | 中 |
| Q010 | [给你 7B 参数预算，如何从零设计 Decoder-only 架构？](./questions/01-transformer-architecture/010.md) | Transformer 与模型架构 | B 类等价追问题 | ★★★★★ | 难 |
| Q011 | [BPE、WordPiece、SentencePiece 的本质区别？](./questions/02-tokenizer-data/011.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★☆ | 中 |
| Q012 | [Vocabulary Size 应该怎么定？](./questions/02-tokenizer-data/012.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★☆ | 中 |
| Q013 | [什么是 Tokenizer Fertility？为什么中文/多语言必须看？](./questions/02-tokenizer-data/013.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★☆☆ | 中 |
| Q014 | [从 Common Crawl 到训练 Token：完整预训练数据 Pipeline 怎么设计？](./questions/02-tokenizer-data/014.md) | Tokenizer 与预训练数据 | A 类高频真题型 | ★★★★★ | 难 |
| Q015 | [Exact Dedup、MinHash、SimHash、Semantic Dedup 分别解决什么？](./questions/02-tokenizer-data/015.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★★ | 中 |
| Q016 | [预训练数据为什么不能简单追求“质量越高越好”？](./questions/02-tokenizer-data/016.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★☆ | 中 |
| Q017 | [预训练数据 Mixture 到底怎么调？](./questions/02-tokenizer-data/017.md) | Tokenizer 与预训练数据 | A 类高频真题型 | ★★★★★ | 难 |
| Q018 | [什么是 Benchmark Contamination？如何系统检测？](./questions/02-tokenizer-data/018.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★★ | 难 |
| Q019 | [Packing 与 Padding 有什么区别？为什么 Packing 不是简单拼接？](./questions/02-tokenizer-data/019.md) | Tokenizer 与预训练数据 | A 类高频真题型 | ★★★★★ | 中 |
| Q020 | [Synthetic Data 在预训练阶段的价值与风险是什么？](./questions/02-tokenizer-data/020.md) | Tokenizer 与预训练数据 | B 类等价追问题 | ★★★★★ | 中 |
| Q021 | [Causal LM Loss 是什么？为什么 Next-Token Prediction 能学出复杂能力？](./questions/03-objective-optimizer/021.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★★ | 中 |
| Q022 | [为什么训练能并行预测所有 Token，而推理必须逐 Token 生成？](./questions/03-objective-optimizer/022.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★☆ | 易 |
| Q023 | [AdamW 为什么长期是 LLM 预训练默认优化器？](./questions/03-objective-optimizer/023.md) | 目标函数、Optimizer 与 Training Recipe | A 类高频真题型 | ★★★★★ | 中 |
| Q024 | [为什么大模型训练需要 Learning-Rate Warmup？](./questions/03-objective-optimizer/024.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★☆ | 中 |
| Q025 | [Cosine Decay 为什么常见？Continued Pretraining 如何重设 LR？](./questions/03-objective-optimizer/025.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★☆ | 中 |
| Q026 | [Batch Size 增大后，优化和系统分别发生什么？](./questions/03-objective-optimizer/026.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★☆ | 中 |
| Q027 | [Global Batch、Micro Batch、Gradient Accumulation 如何换算？](./questions/03-objective-optimizer/027.md) | 目标函数、Optimizer 与 Training Recipe | A 类高频真题型 | ★★★★★ | 易 |
| Q028 | [Weight Decay 为什么通常不施加到所有参数？](./questions/03-objective-optimizer/028.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★☆☆ | 中 |
| Q029 | [为什么 Label Smoothing 不是 LLM 预训练的默认配置？](./questions/03-objective-optimizer/029.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★☆☆ | 中 |
| Q030 | [Multi-Token Prediction（MTP）为什么重新受到重视？](./questions/03-objective-optimizer/030.md) | 目标函数、Optimizer 与 Training Recipe | B 类等价追问题 | ★★★★☆ | 难 |
| Q031 | [什么是 Scaling Law？预训练团队为什么需要它？](./questions/04-scaling-law/031.md) | Scaling Law 与预算设计 | A 类高频真题型 | ★★★★★ | 难 |
| Q032 | [Kaplan Scaling 与 Chinchilla 的关键差异是什么？](./questions/04-scaling-law/032.md) | Scaling Law 与预算设计 | A 类高频真题型 | ★★★★★ | 中 |
| Q033 | [为什么今天很多模型会“过训练”更小的参数规模？](./questions/04-scaling-law/033.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★★☆ | 难 |
| Q034 | [为什么训练 FLOPs 常粗略写成 6ND？](./questions/04-scaling-law/034.md) | Scaling Law 与预算设计 | A 类高频真题型 | ★★★★★ | 中 |
| Q035 | [给定固定 GPU-hours，如何决定模型大小和 Token 数？](./questions/04-scaling-law/035.md) | Scaling Law 与预算设计 | A 类高频真题型 | ★★★★★ | 难 |
| Q036 | [为什么 1B 模型的最优超参不能原样搬到 100B？](./questions/04-scaling-law/036.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★★☆ | 难 |
| Q037 | [如何用小模型实验预测大模型最终 Loss？](./questions/04-scaling-law/037.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★★☆ | 难 |
| Q038 | [Loss 平滑 Scaling，为什么能力可能出现阈值或跳变？](./questions/04-scaling-law/038.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★☆☆ | 难 |
| Q039 | [同样 FLOPs 下，Dense 与 MoE 怎么公平比较？](./questions/04-scaling-law/039.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★★★ | 难 |
| Q040 | [Scaling Law 能否用于 Data Mixture 优化？](./questions/04-scaling-law/040.md) | Scaling Law 与预算设计 | B 类等价追问题 | ★★★★☆ | 难 |
| Q041 | [DDP 到底做了什么？](./questions/05-distributed-training/041.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 易 |
| Q042 | [Tensor Parallel 如何切 Transformer？](./questions/05-distributed-training/042.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 难 |
| Q043 | [为什么 TP 通常限制在 NVLink/NVSwitch 高速域？](./questions/05-distributed-training/043.md) | 分布式训练 | B 类等价追问题 | ★★★★☆ | 中 |
| Q044 | [Pipeline Parallel 为什么有 Bubble？1F1B 如何改善？](./questions/05-distributed-training/044.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 中 |
| Q045 | [为什么 1F1B 比 All-Forward-Then-Backward 更省 Activation Memory？](./questions/05-distributed-training/045.md) | 分布式训练 | B 类等价追问题 | ★★★★☆ | 中 |
| Q046 | [ZeRO-1、ZeRO-2、ZeRO-3 分别 Shard 什么？](./questions/05-distributed-training/046.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 易 |
| Q047 | [FSDP 与 ZeRO-3 有什么关系和区别？](./questions/05-distributed-training/047.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 中 |
| Q048 | [Sequence Parallel 与 Context Parallel 有什么区别？](./questions/05-distributed-training/048.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 难 |
| Q049 | [Expert Parallel 为什么需要 All-to-All？](./questions/05-distributed-training/049.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 中 |
| Q050 | [给你 1024 张 GPU，TP/PP/DP/CP/EP 怎么设计？](./questions/05-distributed-training/050.md) | 分布式训练 | A 类高频真题型 | ★★★★★ | 难 |
| Q051 | [7B 模型 BF16 参数本身占多少显存？为什么训练远不止这些？](./questions/06-memory-precision-performance/051.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 易 |
| Q052 | [Adam 混合精度训练每参数到底多少 Bytes？](./questions/06-memory-precision-performance/052.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 中 |
| Q053 | [Activation Memory 和 Parameter Memory 谁更大？](./questions/06-memory-precision-performance/053.md) | 显存、数值精度与性能 | B 类等价追问题 | ★★★★★ | 中 |
| Q054 | [Activation Checkpointing 的原理与代价是什么？](./questions/06-memory-precision-performance/054.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 易 |
| Q055 | [为什么 BF16 通常比 FP16 更适合 LLM 预训练？](./questions/06-memory-precision-performance/055.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 易 |
| Q056 | [FP8 Training 的核心难点是什么？](./questions/06-memory-precision-performance/056.md) | 显存、数值精度与性能 | B 类等价追问题 | ★★★★☆ | 难 |
| Q057 | [什么是 Arithmetic Intensity？为什么 LLM 工程必须懂？](./questions/06-memory-precision-performance/057.md) | 显存、数值精度与性能 | B 类等价追问题 | ★★★★☆ | 中 |
| Q058 | [FlashAttention 为什么快？它是不是近似 Attention？](./questions/06-memory-precision-performance/058.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 中 |
| Q059 | [为什么减少理论 FLOPs 不一定减少 Wall-Clock？](./questions/06-memory-precision-performance/059.md) | 显存、数值精度与性能 | B 类等价追问题 | ★★★★★ | 中 |
| Q060 | [什么是 MFU？MFU 低应该怎样定位？](./questions/06-memory-precision-performance/060.md) | 显存、数值精度与性能 | A 类高频真题型 | ★★★★★ | 中 |
| Q061 | [MoE 为什么能“总参数很大、每 Token FLOPs 较小”？](./questions/07-moe/061.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★★ | 易 |
| Q062 | [Top-1 与 Top-2 Routing 有什么 Trade-off？](./questions/07-moe/062.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★☆ | 中 |
| Q063 | [为什么 MoE 会出现 Expert Collapse / Hot Expert？](./questions/07-moe/063.md) | Mixture-of-Experts | A 类高频真题型 | ★★★★★ | 难 |
| Q064 | [Load-Balancing Auxiliary Loss 怎么工作？为什么太强会伤模型？](./questions/07-moe/064.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★☆ | 难 |
| Q065 | [DeepSeek-V3 的 Auxiliary-Loss-Free Load Balancing 为什么重要？](./questions/07-moe/065.md) | Mixture-of-Experts | A 类高频真题型 | ★★★★★ | 难 |
| Q066 | [Shared Expert 的意义是什么？](./questions/07-moe/066.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★☆ | 中 |
| Q067 | [Fine-Grained Experts 为什么可能优于少量大 Experts？](./questions/07-moe/067.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★☆ | 难 |
| Q068 | [Expert Parallel 与 Tensor Parallel 如何相互影响？](./questions/07-moe/068.md) | Mixture-of-Experts | B 类等价追问题 | ★★★★★ | 难 |
| Q069 | [MoE 为什么特别容易 Communication-Bound？](./questions/07-moe/069.md) | Mixture-of-Experts | A 类高频真题型 | ★★★★★ | 难 |
| Q070 | [Qwen3 MoE 与 DeepSeek-V3 MoE 应该怎样专业比较？](./questions/07-moe/070.md) | Mixture-of-Experts | A 类高频真题型 | ★★★★★ | 难 |
| Q071 | [Self-Attention 为什么是 O(S²)？](./questions/08-long-context/071.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★☆ | 易 |
| Q072 | [FlashAttention 解决的是计算复杂度还是 IO Complexity？](./questions/08-long-context/072.md) | 长上下文与高效 Attention | A 类高频真题型 | ★★★★★ | 易 |
| Q073 | [RoPE 为什么会有 Length Extrapolation 问题？](./questions/08-long-context/073.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★★ | 难 |
| Q074 | [NTK-Aware Scaling / YaRN 本质上在做什么？](./questions/08-long-context/074.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★☆ | 难 |
| Q075 | [为什么 Long-Context 通常还需要 Continued Pretraining？](./questions/08-long-context/075.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★★ | 中 |
| Q076 | [Context 从 4K 扩到 32K，为什么常采用阶段式训练？](./questions/08-long-context/076.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★☆ | 中 |
| Q077 | [Sliding-Window Attention 的优缺点是什么？](./questions/08-long-context/077.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★☆ | 中 |
| Q078 | [用了 FlashAttention 为什么长上下文训练仍然 OOM？](./questions/08-long-context/078.md) | 长上下文与高效 Attention | A 类高频真题型 | ★★★★★ | 中 |
| Q079 | [Context Parallel 下 Attention 是怎么计算的？](./questions/08-long-context/079.md) | 长上下文与高效 Attention | A 类高频真题型 | ★★★★★ | 难 |
| Q080 | [如何证明一个“128K 模型”真的有 128K 有效能力？](./questions/08-long-context/080.md) | 长上下文与高效 Attention | B 类等价追问题 | ★★★★☆ | 难 |
| Q081 | [100B 模型训练到 42k Step 突然 Loss Spike，怎么排查？](./questions/09-stability-debug-eval/081.md) | 训练稳定性、Debug 与评测 | A 类高频真题型 | ★★★★★ | 难 |
| Q082 | [如何区分 Bad Batch 与 Optimizer Instability？](./questions/09-stability-debug-eval/082.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★★ | 难 |
| Q083 | [Gradient Norm 突然变大意味着什么？](./questions/09-stability-debug-eval/083.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★☆ | 中 |
| Q084 | [Overall Loss 在降，但 Math/Code Benchmark 不涨，为什么？](./questions/09-stability-debug-eval/084.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★★ | 中 |
| Q085 | [Training/Validation Loss 都下降，就能说明模型更好吗？](./questions/09-stability-debug-eval/085.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★☆ | 中 |
| Q086 | [如何监控 1000+ GPU 的预训练任务？](./questions/09-stability-debug-eval/086.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★★ | 难 |
| Q087 | [单个 GPU 比其他 GPU 慢 20%，整个 Job 会怎样？](./questions/09-stability-debug-eval/087.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★☆ | 中 |
| Q088 | [训练出现 NaN，你的排查顺序是什么？](./questions/09-stability-debug-eval/088.md) | 训练稳定性、Debug 与评测 | A 类高频真题型 | ★★★★★ | 中 |
| Q089 | [Checkpoint 应保存什么，才能做到真正可恢复？](./questions/09-stability-debug-eval/089.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★★ | 难 |
| Q090 | [如何定义一个预训练模型“训练成功”？](./questions/09-stability-debug-eval/090.md) | 训练稳定性、Debug 与评测 | B 类等价追问题 | ★★★★☆ | 中 |
| Q091 | [手写 Multi-Head Attention，面试官真正看什么？](./questions/10-coding-system-project/091.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 中 |
| Q092 | [手写 Causal Mask：如何保证语义和数值都正确？](./questions/10-coding-system-project/092.md) | 手撕、系统设计与项目拷打 | B 类等价追问题 | ★★★★☆ | 易 |
| Q093 | [手写 RMSNorm：最常见错误是什么？](./questions/10-coding-system-project/093.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★☆ | 易 |
| Q094 | [手写 RoPE：代码之外必须证明什么？](./questions/10-coding-system-project/094.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 难 |
| Q095 | [手算一个 Transformer Block 的参数量怎么做？](./questions/10-coding-system-project/095.md) | 手撕、系统设计与项目拷打 | B 类等价追问题 | ★★★★★ | 中 |
| Q096 | [手算 70B + Adam + BF16 的训练显存，并推到 ZeRO](./questions/10-coding-system-project/096.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 难 |
| Q097 | [从 0 预训练一个 1B 模型，完整 Pipeline 如何设计？](./questions/10-coding-system-project/097.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 难 |
| Q098 | [1000 张 GPU 给你一个月，怎样降低 Full Run 失败概率？](./questions/10-coding-system-project/098.md) | 手撕、系统设计与项目拷打 | B 类等价追问题 | ★★★★★ | 难 |
| Q099 | [面试官问“你真的从 0 预训练过模型吗？”怎样证明？](./questions/10-coding-system-project/099.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 中 |
| Q100 | [你在预训练项目中真正解决的最难问题是什么？](./questions/10-coding-system-project/100.md) | 手撕、系统设计与项目拷打 | A 类高频真题型 | ★★★★★ | 难 |
