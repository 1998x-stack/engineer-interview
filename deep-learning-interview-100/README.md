# Deep Learning Interview 100 · 2026

一套面向 **深度学习 / 大模型 / 多模态 / CV / 搜推算法工程师** 的系统化面试题库。仓库由《深度学习算法岗面试 100 题 · 2026 版》PDF 重构而来。**v2-deep** 已对 100 个 Markdown 逐题二次扩写：除数学推导、Tensor Shape、PyTorch 验证、工程边界与连续追问外，新增题目特定实验、90 分深挖、项目化证据链、指标卡、停止条件和 5 分钟白板展开路线。

> 设计理念：**先答题 → 看标准回答 → 原理拆解 → 数学/Shape → 工程实现 → 连续追问 → 复盘失分点**。借鉴“以题带知识、层层追问”的训练方法，不复刻《剑指 Offer》的原文、题目或版式。

## 仓库特点

- **100 道题，100 个 Markdown**：每道题可独立学习、review、提 issue。
- **2026 能力结构**：不仅覆盖 BN/LN、CNN、Transformer，也覆盖 LoRA、SFT、PPO/DPO/GRPO、FlashAttention、FSDP/ZeRO、vLLM 与线上排障。
- **面试导向**：每题都有 60–90 秒口述答案、追问链、失分点、自测清单。
- **工程导向**：每题都有题目特定验证协议；重点题给出 PyTorch 实现、shape invariant、显存/复杂度公式和故障诊断框架。
- **项目导向**：新增“项目化证据链”，要求用 metric、ablation、profiling、slice 或线上数据证明结论。
- **90 分深挖**：每题补充机制与定量抓手、失败边界、白板专项练习和 5 分钟展开路线。
- **可维护**：元数据、自动索引、内容深度 CI、MkDocs 配置齐全。

## 能力地图

```mermaid
flowchart LR
  A[数学与反向传播] --> B[优化与稳定性]
  B --> C[CNN / Sequence]
  C --> D[Transformer]
  D --> E[LoRA / SFT / RL]
  D --> F[多模态 / Diffusion]
  E --> G[分布式训练]
  F --> G
  G --> H[推理与 Serving]
  H --> I[项目系统设计]
```

## 推荐使用方式

1. **第一遍：只看标题。** 每题限时 60–90 秒口述。
2. **第二遍：重写公式。** 不复制答案，自己写 tensor shape / 梯度 / 复杂度。
3. **第三遍：连续追问。** 每个追问 30–60 秒，训练被打断后的恢复能力。
4. **第四遍：工程化。** 手写 MHA、InfoNCE、Loss Mask、KV Cache 估算、OOM/NaN/P99 排障。

快速路线见：[7 / 14 / 30 天训练计划](docs/study-plans.md)。只剩一周时直接刷：[Top 30 必刷题](docs/top30.md)。

## 目录结构

```text
deep-learning-interview-100/
├── README.md
├── questions/
│   ├── 01-foundations/                 # Q001-Q010
│   ├── 02-optimization-normalization/  # Q011-Q020
│   ├── 03-cnn-cv/                      # Q021-Q030
│   ├── 04-sequence-language-models/    # Q031-Q038
│   ├── 05-transformer/                 # Q039-Q055
│   ├── 06-llm-post-training/           # Q056-Q068
│   ├── 07-multimodal-diffusion/        # Q069-Q078
│   ├── 08-training-distributed/        # Q079-Q088
│   ├── 09-inference-optimization/      # Q089-Q095
│   └── 10-project-system-design/       # Q096-Q100
├── docs/                               # 学习路线、追问链、评分标准
├── metadata/questions.json             # 机器可读元数据
├── scripts/                            # 自动索引与 QA
├── assets/pdf/                         # 原始完整 PDF
├── .github/workflows/quality.yml
└── mkdocs.yml
```

## 100 题索引

| ID | 题目 | 章节 | 难度 | 优先级 |
|---|---|---|---|---|
| Q001 | [为什么神经网络必须引入非线性激活函数？](questions/01-foundations/Q001-nonlinear-activation.md) | 神经网络与反向传播基础 | ★☆☆ | A |
| Q002 | [反向传播的本质是什么？Autograd 在做什么？](questions/01-foundations/Q002-backprop-autograd.md) | 神经网络与反向传播基础 | ★★☆ | A |
| Q003 | [为什么 Softmax 与 Cross Entropy 常一起使用？请推导梯度。](questions/01-foundations/Q003-softmax-cross-entropy-gradient.md) | 神经网络与反向传播基础 | ★★☆ | A |
| Q004 | [Sigmoid、Tanh、ReLU、GELU、SiLU 如何比较？](questions/01-foundations/Q004-activation-functions.md) | 神经网络与反向传播基础 | ★☆☆ | A |
| Q005 | [什么是梯度消失与梯度爆炸？如何系统解决？](questions/01-foundations/Q005-vanishing-exploding-gradients.md) | 神经网络与反向传播基础 | ★★☆ | S |
| Q006 | [Xavier 与 Kaiming 初始化为什么有效？](questions/01-foundations/Q006-xavier-kaiming-init.md) | 神经网络与反向传播基础 | ★★☆ | A |
| Q007 | [什么是过拟合？如何判断与治理？](questions/01-foundations/Q007-overfitting.md) | 神经网络与反向传播基础 | ★☆☆ | A |
| Q008 | [Label Smoothing 为什么有效？什么时候可能有副作用？](questions/01-foundations/Q008-label-smoothing.md) | 神经网络与反向传播基础 | ★★☆ | A |
| Q009 | [MSE、BCE、Cross Entropy 分别用于什么场景？](questions/01-foundations/Q009-loss-functions.md) | 神经网络与反向传播基础 | ★☆☆ | A |
| Q010 | [类别极度不平衡怎么办？指标如何选？](questions/01-foundations/Q010-class-imbalance.md) | 神经网络与反向传播基础 | ★★☆ | A |
| Q011 | [SGD、Momentum、RMSProp、Adam 的核心差异是什么？](questions/02-optimization-normalization/Q011-optimizers.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q012 | [Adam 与 AdamW 有什么区别？](questions/02-optimization-normalization/Q012-adam-vs-adamw.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q013 | [为什么某些视觉任务中 SGD 最终泛化可能优于 Adam？](questions/02-optimization-normalization/Q013-sgd-generalization.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q014 | [为什么 Transformer 常用 Learning Rate Warmup？](questions/02-optimization-normalization/Q014-lr-warmup.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q015 | [Cosine Learning Rate Scheduler 为什么常用？](questions/02-optimization-normalization/Q015-cosine-scheduler.md) | 优化器、归一化与正则化 | ★☆☆ | S |
| Q016 | [BatchNorm 的训练与推理过程分别是什么？](questions/02-optimization-normalization/Q016-batchnorm.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q017 | [为什么 Transformer 常用 LayerNorm，而 CNN 传统上大量用 BatchNorm？](questions/02-optimization-normalization/Q017-layernorm-vs-batchnorm.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q018 | [RMSNorm 与 LayerNorm 有什么区别？](questions/02-optimization-normalization/Q018-rmsnorm-vs-layernorm.md) | 优化器、归一化与正则化 | ★★☆ | S |
| Q019 | [Pre-Norm 与 Post-Norm 的区别是什么？为什么 Pre-Norm 更易训练深层网络？](questions/02-optimization-normalization/Q019-prenorm-vs-postnorm.md) | 优化器、归一化与正则化 | ★★★ | S |
| Q020 | [Dropout 为什么能防止过拟合？训练和推理如何处理？](questions/02-optimization-normalization/Q020-dropout.md) | 优化器、归一化与正则化 | ★☆☆ | S |
| Q021 | [给定卷积参数，如何计算输出尺寸与参数量？](questions/03-cnn-cv/Q021-conv-output-params.md) | CNN 与计算机视觉基础 | ★☆☆ | A |
| Q022 | [什么是感受野？如何计算多层网络的有效感受野？](questions/03-cnn-cv/Q022-receptive-field.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q023 | [1×1 卷积有什么作用？](questions/03-cnn-cv/Q023-conv-1x1.md) | CNN 与计算机视觉基础 | ★☆☆ | A |
| Q024 | [Depthwise Separable Convolution 为什么更省计算？](questions/03-cnn-cv/Q024-depthwise-separable-conv.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q025 | [ResNet 为什么能训练很深？](questions/03-cnn-cv/Q025-resnet.md) | CNN 与计算机视觉基础 | ★★☆ | S |
| Q026 | [Batch 很小时为什么 BatchNorm 容易失效？有哪些替代？](questions/03-cnn-cv/Q026-small-batch-normalization.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q027 | [IoU 与 NMS 分别是什么？请说明 NMS 实现细节。](questions/03-cnn-cv/Q027-iou-nms.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q028 | [Focal Loss 为什么能处理前景/背景极度不平衡？](questions/03-cnn-cv/Q028-focal-loss.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q029 | [ViT 与 CNN 的本质差异是什么？](questions/03-cnn-cv/Q029-vit-vs-cnn.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q030 | [数据增强为什么有效？Mixup 与 CutMix 有什么不同？](questions/03-cnn-cv/Q030-mixup-cutmix.md) | CNN 与计算机视觉基础 | ★★☆ | A |
| Q031 | [RNN、LSTM、GRU 的主要区别是什么？](questions/04-sequence-language-models/Q031-rnn-lstm-gru.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q032 | [为什么 LSTM 能缓解梯度消失？](questions/04-sequence-language-models/Q032-lstm-gradient.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q033 | [Teacher Forcing 有什么问题？](questions/04-sequence-language-models/Q033-teacher-forcing.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q034 | [BERT 的预训练目标是什么？为什么它适合理解类任务？](questions/04-sequence-language-models/Q034-bert-pretraining.md) | 序列模型与语言模型基础 | ★☆☆ | A |
| Q035 | [Encoder-only、Decoder-only、Encoder-Decoder 如何选择？](questions/04-sequence-language-models/Q035-transformer-architectures.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q036 | [BPE、WordPiece、SentencePiece 为什么存在？](questions/04-sequence-language-models/Q036-tokenization.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q037 | [Padding Token 为什么通常不参与 Loss？](questions/04-sequence-language-models/Q037-padding-loss-mask.md) | 序列模型与语言模型基础 | ★☆☆ | A |
| Q038 | [Causal Mask 与 Padding Mask 有什么区别？](questions/04-sequence-language-models/Q038-causal-padding-mask.md) | 序列模型与语言模型基础 | ★★☆ | A |
| Q039 | [从头讲一个现代 Transformer Block。](questions/05-transformer/Q039-transformer-block.md) | Transformer 核心 | ★★☆ | S |
| Q040 | [写出 Scaled Dot-Product Attention，并解释每一步。](questions/05-transformer/Q040-scaled-dot-product-attention.md) | Transformer 核心 | ★★☆ | S |
| Q041 | [为什么 Attention 要除以 √d_k？](questions/05-transformer/Q041-attention-scaling.md) | Transformer 核心 | ★★☆ | S |
| Q042 | [Q、K、V 从语义和线性代数上分别是什么？](questions/05-transformer/Q042-qkv.md) | Transformer 核心 | ★★☆ | S |
| Q043 | [Self-Attention 的时间和显存复杂度是多少？](questions/05-transformer/Q043-attention-complexity.md) | Transformer 核心 | ★★☆ | S |
| Q044 | [Multi-Head Attention 为什么比单头更有表达力？](questions/05-transformer/Q044-multi-head-attention.md) | Transformer 核心 | ★★☆ | S |
| Q045 | [为什么 Attention 需要位置编码？](questions/05-transformer/Q045-position-encoding.md) | Transformer 核心 | ★★☆ | S |
| Q046 | [Absolute Position、Relative Position、RoPE 有什么区别？](questions/05-transformer/Q046-rope-relative-position.md) | Transformer 核心 | ★★★ | S |
| Q047 | [Transformer 的 FFN 到底做什么？为什么不能删？](questions/05-transformer/Q047-transformer-ffn.md) | Transformer 核心 | ★★☆ | S |
| Q048 | [MHA、MQA、GQA 的区别？为什么 GQA 能省 KV Cache？](questions/05-transformer/Q048-mha-mqa-gqa.md) | Transformer 核心 | ★★★ | S |
| Q049 | [KV Cache 的原理是什么？显存如何估算？](questions/05-transformer/Q049-kv-cache.md) | Transformer 核心 | ★★★ | S |
| Q050 | [FlashAttention 为什么快？它有没有把 O(T²) 变成 O(T)？](questions/05-transformer/Q050-flashattention.md) | Transformer 核心 | ★★★ | S |
| Q051 | [Sparse Attention / Sliding Window Attention 为什么有用？](questions/05-transformer/Q051-sparse-sliding-window-attention.md) | Transformer 核心 | ★★☆ | S |
| Q052 | [为什么现代通用大模型大量采用 Decoder-only？](questions/05-transformer/Q052-decoder-only.md) | Transformer 核心 | ★★☆ | S |
| Q053 | [Transformer 相比 RNN 为什么更适合大规模训练？](questions/05-transformer/Q053-transformer-vs-rnn.md) | Transformer 核心 | ★★☆ | S |
| Q054 | [长上下文模型真正面临哪些问题？](questions/05-transformer/Q054-long-context.md) | Transformer 核心 | ★★★ | S |
| Q055 | [请手写 Multi-Head Attention，必须处理 shape、mask 与数值稳定。](questions/05-transformer/Q055-implement-mha.md) | Transformer 核心 | ★★★ | S |
| Q056 | [LoRA 的数学原理是什么？为什么低秩更新可行？](questions/06-llm-post-training/Q056-lora.md) | LoRA、SFT 与大模型后训练 | ★★☆ | S |
| Q057 | [LoRA Rank 怎么选？为什么经典初始化常让一侧为零？](questions/06-llm-post-training/Q057-lora-rank-init.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q058 | [QLoRA 与 LoRA 的区别是什么？4-bit 基座为什么还能训练？](questions/06-llm-post-training/Q058-qlora.md) | LoRA、SFT 与大模型后训练 | ★★☆ | S |
| Q059 | [Full Fine-tuning 与 LoRA 应该如何选择？](questions/06-llm-post-training/Q059-full-ft-vs-lora.md) | LoRA、SFT 与大模型后训练 | ★★☆ | S |
| Q060 | [SFT 的完整数据流程应该怎么设计？](questions/06-llm-post-training/Q060-sft-data-pipeline.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q061 | [SFT 时如何设计 Label Mask？为什么 user prompt 常不计算 Loss？](questions/06-llm-post-training/Q061-sft-label-mask.md) | LoRA、SFT 与大模型后训练 | ★★☆ | S |
| Q062 | [SFT Loss 剧烈震荡或突然 NaN，如何排查？](questions/06-llm-post-training/Q062-sft-loss-debug.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q063 | [经典 PPO-based RLHF 由哪些模型组成？目标是什么？](questions/06-llm-post-training/Q063-ppo-rlhf.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q064 | [DPO 为什么不需要显式 Reward Model 与在线 RL？](questions/06-llm-post-training/Q064-dpo.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q065 | [GRPO 相比 PPO 的关键变化是什么？优势估计从哪里来？](questions/06-llm-post-training/Q065-grpo.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q066 | [RLHF / GRPO 为什么常需要 KL Constraint？](questions/06-llm-post-training/Q066-kl-constraint.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q067 | [什么是 Reward Hacking？如何发现与抑制？](questions/06-llm-post-training/Q067-reward-hacking.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q068 | [如何判断 RL/Post-training 训练“达标”？](questions/06-llm-post-training/Q068-post-training-evaluation.md) | LoRA、SFT 与大模型后训练 | ★★★ | S |
| Q069 | [InfoNCE Loss 是什么？为什么适合对比学习？](questions/07-multimodal-diffusion/Q069-infonce.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q070 | [InfoNCE 中 Temperature τ 起什么作用？](questions/07-multimodal-diffusion/Q070-temperature.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q071 | [对比学习中的 False Negative 如何处理？](questions/07-multimodal-diffusion/Q071-false-negative.md) | 对比学习、多模态与 Diffusion | ★★★ | A |
| Q072 | [CLIP 为什么能做 Zero-shot 分类？](questions/07-multimodal-diffusion/Q072-clip-zero-shot.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q073 | [如何把 Text-only LLM 改造成多模态模型？](questions/07-multimodal-diffusion/Q073-multimodal-llm.md) | 对比学习、多模态与 Diffusion | ★★★ | A |
| Q074 | [多模态模型如何处理视频？视觉 token 爆炸怎么办？](questions/07-multimodal-diffusion/Q074-video-multimodal.md) | 对比学习、多模态与 Diffusion | ★★★ | A |
| Q075 | [Diffusion 的 Forward Process 是什么？](questions/07-multimodal-diffusion/Q075-diffusion-forward.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q076 | [Diffusion 为什么经常预测 Noise？](questions/07-multimodal-diffusion/Q076-diffusion-noise-prediction.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q077 | [Latent Diffusion 为什么比 Pixel Diffusion 更便宜？](questions/07-multimodal-diffusion/Q077-latent-diffusion.md) | 对比学习、多模态与 Diffusion | ★★☆ | A |
| Q078 | [U-Net Diffusion 与 DiT 有什么区别？](questions/07-multimodal-diffusion/Q078-dit-vs-unet.md) | 对比学习、多模态与 Diffusion | ★★★ | A |
| Q079 | [FP16、BF16、FP32 的差异是什么？为什么大模型偏爱 BF16？](questions/08-training-distributed/Q079-fp16-bf16-fp32.md) | 训练工程与分布式训练 | ★★☆ | S |
| Q080 | [Mixed Precision 为什么能提速？Loss Scaling 的作用是什么？](questions/08-training-distributed/Q080-mixed-precision.md) | 训练工程与分布式训练 | ★★☆ | S |
| Q081 | [Gradient Accumulation 如何得到更大的 Effective Batch？](questions/08-training-distributed/Q081-gradient-accumulation.md) | 训练工程与分布式训练 | ★☆☆ | S |
| Q082 | [Gradient Checkpointing 为什么能省显存？代价是什么？](questions/08-training-distributed/Q082-gradient-checkpointing.md) | 训练工程与分布式训练 | ★★☆ | S |
| Q083 | [DDP 的核心原理是什么？为什么每卡模型保持一致？](questions/08-training-distributed/Q083-ddp.md) | 训练工程与分布式训练 | ★★☆ | S |
| Q084 | [ZeRO-1/2/3 与 FSDP 的核心区别和关系是什么？](questions/08-training-distributed/Q084-zero-fsdp.md) | 训练工程与分布式训练 | ★★★ | S |
| Q085 | [Data Parallel、Tensor Parallel、Pipeline Parallel 怎么区分？](questions/08-training-distributed/Q085-parallelism.md) | 训练工程与分布式训练 | ★★★ | S |
| Q086 | [CUDA OOM 怎么系统排查，而不是只减 batch？](questions/08-training-distributed/Q086-cuda-oom.md) | 训练工程与分布式训练 | ★★★ | S |
| Q087 | [Loss 变 NaN/Inf，如何定位根因？](questions/08-training-distributed/Q087-nan-inf-debug.md) | 训练工程与分布式训练 | ★★★ | S |
| Q088 | [GPU 利用率只有 30%，如何排查？](questions/08-training-distributed/Q088-gpu-utilization.md) | 训练工程与分布式训练 | ★★★ | S |
| Q089 | [INT8/INT4 Quantization 为什么能省显存并可能加速？](questions/09-inference-optimization/Q089-quantization.md) | 模型压缩与推理优化 | ★★☆ | S |
| Q090 | [PTQ 与 QAT 有什么区别？](questions/09-inference-optimization/Q090-ptq-vs-qat.md) | 模型压缩与推理优化 | ★★☆ | S |
| Q091 | [vLLM / PagedAttention 解决了什么问题？](questions/09-inference-optimization/Q091-vllm-pagedattention.md) | 模型压缩与推理优化 | ★★★ | S |
| Q092 | [Continuous Batching 为什么能提高 LLM Serving 吞吐？](questions/09-inference-optimization/Q092-continuous-batching.md) | 模型压缩与推理优化 | ★★☆ | S |
| Q093 | [Prefill 与 Decode 的性能特征有什么区别？](questions/09-inference-optimization/Q093-prefill-decode.md) | 模型压缩与推理优化 | ★★★ | S |
| Q094 | [Speculative Decoding 的原理是什么？为什么能保持目标模型分布？](questions/09-inference-optimization/Q094-speculative-decoding.md) | 模型压缩与推理优化 | ★★★ | S |
| Q095 | [线上 LLM 突然变慢，如何分层定位？](questions/09-inference-optimization/Q095-llm-latency-debug.md) | 模型压缩与推理优化 | ★★★ | S |
| Q096 | [项目中为什么选择这个模型，而不是另一个模型？](questions/10-project-system-design/Q096-model-selection.md) | 项目深挖与系统题 | ★★★ | S |
| Q097 | [Offline 指标提升，Online 指标为什么可能下降？](questions/10-project-system-design/Q097-offline-online-gap.md) | 项目深挖与系统题 | ★★★ | S |
| Q098 | [什么是 Ablation Study？怎样做才有说服力？](questions/10-project-system-design/Q098-ablation-study.md) | 项目深挖与系统题 | ★★☆ | S |
| Q099 | [训练 Loss 一直下降，但验证指标不涨，怎么办？](questions/10-project-system-design/Q099-train-loss-val-metric.md) | 项目深挖与系统题 | ★★★ | S |
| Q100 | [现场从零实现 Attention / BN / InfoNCE，面试官真正考什么？](questions/10-project-system-design/Q100-implement-from-scratch.md) | 项目深挖与系统题 | ★★★ | S |

## 原始 PDF

- [《深度学习算法岗面试 100 题 · 2026 版》](assets/pdf/deep_learning_algorithm_interview_100_2026.pdf)

## 质量原则

这个仓库刻意避免三种“伪掌握”：

1. 只背定义，不知道为什么；
2. 会公式，不会 tensor shape / 边界；
3. 离线会炼丹，线上不会定位 OOM、NaN、P99 和 train-serving skew。

详见 [回答评分标准](docs/interview-rubric.md)、[内容质量标准](docs/content-quality.md) 与 [仓库方法论](docs/source-methodology.md)。

## 本地 QA

```bash
python scripts/check_repo.py
python scripts/build_index.py --check
```

## 本地文档站点

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 内容边界

“真题”指公开候选人面经中出现的真实问法经过归一化后的训练题，不声称来自企业官方题库，也不包含任何非公开或保密面试材料。
