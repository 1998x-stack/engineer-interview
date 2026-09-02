# 09 vLLM / SGLang / TensorRT-LLM

把框架理解为 scheduler + cache manager + executor + kernels + distributed runtime 的组合。

## 本章学习方法

- **问题范围**：Q081 - Q090
- **核心实验**：同一模型同一 workload 在两个 runtime 上跑统一 benchmark schema，比较 Goodput 与 p99，而非只看峰值 tokens/s。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q081 请描述 vLLM 的核心架构思想。](q081-vllm-architecture.md) - ★★★★★ - `vLLM, architecture`
- [Q082 vLLM V1 Scheduler 与早期设计有什么重要变化？](q082-vllm-v1-scheduler.md) - ★★★★★ - `vLLM-V1, scheduler`
- [Q083 SGLang RadixAttention 相比普通 Prefix Caching 的核心优势？](q083-sglang-radixattention.md) - ★★★★★ - `SGLang, RadixAttention`
- [Q084 TensorRT-LLM 和 vLLM 怎么选？](q084-framework-selection-trtllm-vllm.md) - ★★★★★ - `framework-selection, TRTLLM, vLLM`
- [Q085 TensorRT-LLM 的 KV Cache system 有什么特点？](q085-tensorrt-llm-kv.md) - ★★★★☆ - `TensorRT-LLM, KV`
- [Q086 SGLang HiCache 是什么？](q086-hicache-sglang.md) - ★★★★☆ - `HiCache, SGLang`
- [Q087 Multi-LoRA Serving 怎么优化？](q087-lora-serving.md) - ★★★★☆ - `LoRA, serving`
- [Q088 Structured Output 为什么会影响推理性能？](q088-structured-output-fsm.md) - ★★★★☆ - `structured-output, FSM`
- [Q089 为什么模型刚启动时延迟明显更高？](q089-cold-start-startup.md) - ★★★★☆ - `cold-start, startup`
- [Q090 如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？](q090-framework-selection-production.md) - ★★★★★ - `framework-selection, production`
