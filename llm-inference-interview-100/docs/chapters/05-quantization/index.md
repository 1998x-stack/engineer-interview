# 05 量化与低精度推理

同时优化精度、内存、带宽和硬件 kernel，而不是把 bit-width 当成性能答案。

## 本章学习方法

- **问题范围**：Q041 - Q050
- **核心实验**：同一模型比较 BF16、FP8、W4A16；在 batch=1 与高并发下分别测速度，解释 Roofline 变化。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q041 Weight-only Quantization 与 W8A8 有什么区别？](q041-quantization-w4a16-w8a8.md) - ★★★★★ - `quantization, W4A16, W8A8`
- [Q042 GPTQ 原理是什么？](q042-gptq-ptq.md) - ★★★★☆ - `GPTQ, PTQ`
- [Q043 AWQ 和 GPTQ 最大区别是什么？](q043-awq-quantization.md) - ★★★★☆ - `AWQ, quantization`
- [Q044 SmoothQuant 为什么叫“把难度从 Activation 搬到 Weight”？](q044-smoothquant-int8.md) - ★★★★★ - `SmoothQuant, INT8`
- [Q045 FP8 与 INT8 的工程区别是什么？](q045-fp8-int8.md) - ★★★★☆ - `FP8, INT8`
- [Q046 FP4 / NVFP4 为什么到 Blackwell 才更加实用？](q046-fp4-nvfp4-blackwell.md) - ★★★★☆ - `FP4, NVFP4, Blackwell`
- [Q047 Per-tensor、Per-channel、Per-group quantization 怎么选？](q047-quantization-scales.md) - ★★★★☆ - `quantization, scales`
- [Q048 为什么 KV Quantization 和 Weight Quantization 是两个问题？](q048-kv-quant-dynamic.md) - ★★★★★ - `KV-quant, dynamic`
- [Q049 量化后的模型如何正确评估？](q049-quant-eval-quality.md) - ★★★★☆ - `quant-eval, quality`
- [Q050 为什么 INT4 模型有时候不比 FP16 快？](q050-int4-performance.md) - ★★★★★ - `INT4, performance`
