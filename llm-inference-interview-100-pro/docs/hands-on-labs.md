# Hands-on Labs｜把 100 道题变成 20 个可复现实验

这部分用于把面试知识转化成真实系统能力。每个 Lab 都要求保存：硬件拓扑、runtime commit、启动参数、请求 trace、原始 per-request 指标和 profiler trace。

## Lab 01：Prefill / Decode Roofline

- 变量：input/output length、concurrency。
- 输出：TTFT/TPOT、HBM、Tensor Core、算术强度近似。
- 对应：Q001–Q010。

## Lab 02：KV Cache 容量与 Paged Allocation

- 变量：context、page size、GQA/MQA、KV dtype。
- 输出：KV bytes/token、可服务并发、碎片、OOM 点。
- 对应：Q011–Q015、Q018。

## Lab 03：Prefix Reuse / Radix Cache

- 变量：共享前缀比例与长度。
- 输出：hit tokens、TTFT、eviction、GPU KV occupancy。
- 对应：Q016–Q017、Q083、Q086。

## Lab 04：Chunked Prefill 与调度

- 变量：chunk/token budget、arrival rate。
- 输出：TTFT–TPOT Pareto、Goodput、queue。
- 对应：Q021–Q030。

## Lab 05：Attention Kernel IO

- 比较：SDPA / FlashAttention / serving attention backend。
- 输出：HBM bytes、kernel time、长序列 scaling。
- 对应：Q031–Q033。

## Lab 06：Launch / CUDA Graph / Compile

- 变量：batch、shape dynamicity、graph/compile 开关。
- 输出：CPU launch gap、TPOT、compile/capture 开销。
- 对应：Q034–Q040。

## Lab 07：Weight-only Quantization

- 比较：BF16、W8/W4、不同 group size/backend。
- 输出：质量、VRAM、HBM、TPOT。
- 对应：Q041–Q050。

## Lab 08：TP Strong Scaling

- TP=1/2/4/8，固定 workload。
- 输出：compute/collective 占比、scale efficiency。
- 对应：Q051、Q056–Q059。

## Lab 09：PP / DP Capacity

- 比较多种 replica 与 stage 切分。
- 输出：吞吐、bubble、故障域。
- 对应：Q052–Q053。

## Lab 10：Context Parallel Long Context

- context 从 8K 扩到 128K。
- 输出：per-rank KV、通信、TTFT/TPOT。
- 对应：Q055。

## Lab 11：Speculative Decoding

- 变量：draft/spec length、concurrency。
- 输出：accepted tokens/step、verify latency、净 speedup。
- 对应：Q061–Q070。

## Lab 12：MoE Expert Histogram

- 变量：并发、EP、token distribution。
- 输出：tokens/expert、A2A、grouped GEMM shape。
- 对应：Q071–Q080。

## Lab 13：vLLM Scheduler Trace

- 变量：token budget、prefix caching、priority。
- 输出：scheduled tokens、preemption、queue、SLO。
- 对应：Q081–Q082。

## Lab 14：SGLang Prefix / HiCache

- L1-only vs hierarchical cache。
- 输出：tier hit、IO、TTFT。
- 对应：Q083、Q086。

## Lab 15：TensorRT-LLM KV / P-D

- Unified vs disaggregated。
- 输出：KV transfer、TTFT、TPOT、Goodput。
- 对应：Q084–Q085、Q030。

## Lab 16：Multi-LoRA

- 变量：adapter 数、adapter locality、batch。
- 输出：adapter cache、base/LoRA kernel、吞吐。
- 对应：Q087。

## Lab 17：Structured Output

- unconstrained vs grammar constrained。
- 输出：CPU mask time、TPOT、合法率。
- 对应：Q088。

## Lab 18：Cold Start

- 分阶段测 weight load、NCCL init、compile、graph capture。
- 对应：Q089。

## Lab 19：Framework Shootout

- vLLM/SGLang/TensorRT-LLM 同 workload 同硬件。
- 输出：Goodput、运维复杂度、feature fast-path。
- 对应：Q084、Q090。

## Lab 20：Production Regression Drill

- 人为制造 traffic shift、cache miss、慢 rank、版本变化。
- 要求从 dashboard → trace → profiler 找根因。
- 对应：Q091–Q100。
