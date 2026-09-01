# 30 个实现级 Gotchas

> 这些条目来自 PDF 附录 B，并补充“为什么危险”和“如何测”。

| # | Gotcha | 建议验证 |
|---:|---|---|
| 101 | Softmax 维度写错：通常沿 key 维 `dim=-1`。 | 构造 4×4 最小 attention，检查概率和、可见位置与 finite。 |
| 102 | Mask 放在 Softmax 之后。 | 构造 4×4 最小 attention，检查概率和、可见位置与 finite。 |
| 103 | Causal mask 上/下三角方向反。 | 构造 4×4 最小 attention，检查概率和、可见位置与 finite。 |
| 104 | Padding mask 与 loss mask 混为一谈。 | 写一个能在 CI 中稳定复现的最小失败用例。 |
| 105 | left padding 时 position id 未按有效 token 计算。 | 写一个能在 CI 中稳定复现的最小失败用例。 |
| 106 | 整行全 `-inf` 导致 softmax NaN。 | 构造 4×4 最小 attention，检查概率和、可见位置与 finite。 |
| 107 | 漏除 `sqrt(d_head)`。 | 构造 4×4 最小 attention，检查概率和、可见位置与 finite。 |
| 108 | transpose 后直接 view，stride 不连续。 | 打印 shape/stride，并覆盖 B=1,T=1,H=1/GQA。 |
| 109 | 把 `[B,T,H,Dh]` 与 `[B,H,T,Dh]` 混用。 | 打印 shape/stride，并覆盖 B=1,T=1,H=1/GQA。 |
| 110 | GQA 中 Q head 与 KV head group 映射错误。 | 打印 shape/stride，并覆盖 B=1,T=1,H=1/GQA。 |
| 111 | RoPE 在 K cache 追加时 position offset 错。 | full vs incremental parity + cache 长度/reorder 单测。 |
| 112 | KV cache 每步 `torch.cat` 导致 O(T²) 数据搬运。 | full vs incremental parity + cache 长度/reorder 单测。 |
| 113 | cache reset/reorder 在 batch/beam 场景漏处理。 | full vs incremental parity + cache 长度/reorder 单测。 |
| 114 | full forward 与 incremental logits 未做等价性测试。 | full vs incremental parity + cache 长度/reorder 单测。 |
| 115 | 验证时忘记 `model.eval()`。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 116 | AMP gradient clipping 前未 unscale。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 117 | gradient accumulation 忘记正确做 loss normalization。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 118 | scheduler 按 micro-step 而非 optimizer-step 误更新。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 119 | labels 重复 shift 或完全没 shift。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 120 | pad/eos 共用 id 时错误忽略所有 eos loss。 | 固定 batch 跑 2 个 optimizer step，比对 loss/param delta。 |
| 121 | packed sequence 未处理 sample boundary。 | 写一个能在 CI 中稳定复现的最小失败用例。 |
| 122 | fused kernel 与朴素实现 mask 语义不一致。 | 写一个能在 CI 中稳定复现的最小失败用例。 |
| 123 | FlashAttention 被误认为降低数学 O(T²) FLOPs。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 124 | KV cache 内存估算忘记 layers 或 K/V 两份。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 125 | Beam Search KV 内存忘记乘 beam size。 | full vs incremental parity + cache 长度/reorder 单测。 |
| 126 | 只看平均 latency，不看 P99。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 127 | 静态 batch 被最长请求拖住。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 128 | 量化只看 bit 数，不检查 kernel 是否真正支持。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 129 | 多 GPU 只看显存，不看 all-reduce/all-to-all 通信。 | 用 profiler + 显存统计，不用单一 FLOPs/bit 指标判断。 |
| 130 | Tiny overfit 失败时仍继续做大规模训练。 | 写一个能在 CI 中稳定复现的最小失败用例。 |

## Gotcha 排查法

不要把 30 个坑当成 checklist 背诵，应该按故障类型分组。

### A. Shape / Layout

对应：108、109、110。

排查：

```python
print(x.shape, x.stride(), x.is_contiguous())
```

再用非对称尺寸，例如 `B=2,Hq=6,Hkv=2,Tq=3,Tk=5,Dh=8`，避免错误广播“碰巧正确”。

### B. Mask / Softmax

对应：101–107、122。

三个不变量：

1. 非 fully-masked 行概率和≈1；
2. masked key 改值不影响输出；
3. 未来 token 改值不影响过去位置。

### C. KV / Position

对应：111–114、125。

核心 oracle：

```text
full forward logits == incremental cache logits
```

再加入 batch reorder、beam fork、cache reset。

### D. Training Loop

对应：115–120、130。

最小基线：单卡 FP32 + fixed seed + tiny dataset。只有这条路径正确后再开启 AMP、distributed、compile。

### E. Systems / Performance

对应：123–129。

每次性能结论必须记录：

- hardware；
- B/T/H/D；
- dtype；
- kernel/runtime version；
- quality parity；
- P50/P95/P99。

## CI 建议

将高风险 Gotchas 变成自动测试：

- `test_causal_no_future_leakage`；
- `test_padding_invariance`；
- `test_full_vs_cache_logits`；
- `test_fully_masked_row_finite`；
- `test_gqa_head_mapping`；
- `test_tiny_overfit`。

最专业的知识库不是“告诉你哪里会错”，而是把错误变成**无法重新进入主分支的 regression test**。
