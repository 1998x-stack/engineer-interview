# 训练显存手算速查

## 核心原则

任何显存题先声明：

1. 参数 dtype；
2. gradient dtype；
3. 是否维护 FP32 master weights；
4. Adam 一阶/二阶状态 dtype；
5. ZeRO/FSDP stage 与 DP size；
6. TP/PP 是否分片参数；
7. activation 是否 checkpoint；
8. 是否计通信/临时 buffer 与 allocator fragmentation。

## 账本

| 类别 | 典型对象 | 是否会被 ZeRO/FSDP 分片 |
|---|---|---|
| Model weights | BF16/FP16/FP32 参数 | ZeRO-3/FSDP full-shard |
| Gradients | 梯度 | ZeRO-2/3 |
| Optimizer m/v | Adam moments | ZeRO-1/2/3 |
| Master weights | 实现相关 | 通常随 optimizer/state 策略 |
| Activations | layer intermediates | 主要靠 TP/CP/PP/checkpoint |
| Temp buffers | all-gather/GEMM/workspace | 取决于实现，常决定峰值 |

> 不要把“理论持久状态显存”误认为“实际峰值显存”。
