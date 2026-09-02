# 02 KV Cache 与 Attention

把 KV Cache 当作动态内存系统，而不仅是 Transformer 中间张量。

## 本章学习方法

- **问题范围**：Q011 - Q020
- **核心实验**：构造共享 system prompt 与随机 prompt 两组流量，对比 prefix cache hit、TTFT、KV 占用与吞吐。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q011 KV Cache 显存怎么计算？](q011-kv-cache-memory.md) - ★★★★★ - `KV-cache, memory`
- [Q012 MHA、MQA、GQA 为什么会极大影响推理成本？](q012-mha-gqa-mqa.md) - ★★★★☆ - `MHA, GQA, MQA`
- [Q013 PagedAttention 到底解决了什么？](q013-pagedattention-kv.md) - ★★★★★ - `PagedAttention, KV`
- [Q014 KV block/page size 为什么不能无限小？](q014-kv-page-size.md) - ★★★★☆ - `KV, page-size`
- [Q015 什么叫 KV Cache 的 Internal Fragmentation？](q015-fragmentation-kv.md) - ★★★☆☆ - `fragmentation, KV`
- [Q016 Prefix Caching 为什么有时收益巨大，有时几乎没用？](q016-prefix-cache-cache.md) - ★★★★★ - `prefix-cache, cache`
- [Q017 RadixAttention 与普通 Prefix Cache 有什么不同？](q017-sglang-radixattention.md) - ★★★★★ - `SGLang, RadixAttention`
- [Q018 为什么 KV Cache 也值得量化？](q018-kv-quant-fp8.md) - ★★★★★ - `KV-quant, FP8`
- [Q019 Sliding Window Attention 如何降低推理复杂度？](q019-sliding-window-long-context.md) - ★★★★☆ - `sliding-window, long-context`
- [Q020 MLA 为什么对推理优化特别重要？](q020-mla-deepseek.md) - ★★★★★ - `MLA, DeepSeek`
