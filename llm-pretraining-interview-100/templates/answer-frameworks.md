# 面试答题模板

## 架构题

**定义/公式 → 旧方案瓶颈 → 关键设计 → 参数/FLOPs/KV/activation → Trade-off → 可验证实验**

## 分布式题

**切哪个维度 → 每 rank 持什么 → forward/backward collective → 显存变化 → 通信变化 → topology mapping → profile 验证**

## 显存题

**声明 dtype/optimizer → bytes/param → 全局状态 → TP/DP/ZeRO/FSDP 分片 → activation → transient peak**

## 故障题

**First bad step → batch/rank/tensor → replay → hypothesis → controlled experiment → root cause → fix → regression**

## 项目题

**Observation → Hypothesis → Instrumentation → Experiment → Root Cause → Fix → Ablation → Quantitative Result → Next step**
