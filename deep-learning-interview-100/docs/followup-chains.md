# 典型连续追问链

## Attention

`公式 → √d_k → 复杂度 → MHA → MQA/GQA → KV Cache → Decode → FlashAttention → PagedAttention → P99`

建议按顺序刷 [Q040](../questions/05-transformer/Q040-scaled-dot-product-attention.md) → [Q041](../questions/05-transformer/Q041-attention-scaling.md) → [Q043](../questions/05-transformer/Q043-attention-complexity.md) → [Q048](../questions/05-transformer/Q048-mha-mqa-gqa.md) → [Q049](../questions/05-transformer/Q049-kv-cache.md) → [Q050](../questions/05-transformer/Q050-flashattention.md) → [Q091](../questions/09-inference-optimization/Q091-vllm-pagedattention.md) → [Q095](../questions/09-inference-optimization/Q095-llm-latency-debug.md)。

## LoRA / SFT

`ΔW=BA → 参数量 → rank → 初始化 → target modules → QLoRA → Full FT → SFT 数据 → Label Mask → Loss 异常`

## RL / Post-training

`PPO → DPO → GRPO → advantage → KL → reward hacking → evaluation gate`

## 训练故障

`Loss 抖动 → 数据 → LR → grad norm → AMP → 单 rank → OOM → checkpoint → FSDP/ZeRO → GPU util`

## 项目

`为什么选模型 → baseline → 提升来自哪里 → 消融 → offline/online gap → latency/cost → 失败实验 → 资源减半`
