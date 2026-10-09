# CUDA 性能公式与白板推导速查

## 1. Occupancy


\[
Occupancy = \frac{Active\ Warps/SM}{Maximum\ Warps/SM}
\]

Resident blocks 近似由多个资源上限共同取最小值：

\[
B_{resident}=\min(B_{threads}, B_{warps}, B_{registers}, B_{shared}, B_{blockslots})
\]

注意：occupancy 是 latency hiding 的代理，不是最终性能目标。

## 2. Arithmetic Intensity

\[
AI = \frac{FLOPs}{Bytes\ transferred}
\]

Roofline：

\[
P = \min(P_{compute\ peak}, BW_{memory} \times AI)
\]

Ridge point：

\[
AI_{ridge}=\frac{P_{compute\ peak}}{BW_{memory}}
\]

## 3. Effective Bandwidth

\[
BW_{effective}=\frac{Bytes_{useful\ read}+Bytes_{useful\ write}}{time}
\]

例如 N 个 float 从 A 读、向 B 写：

\[
Bytes_{useful} \approx 8N
\]

## 4. Coalescing 白板算法

给出 32 个 lane 地址：

```text
addr[lane] = base + f(lane) * element_size
```

然后：

1. 计算最低/最高地址；
2. 按 transaction/sector 边界划分；
3. 数实际覆盖的 sectors；
4. 比较 `useful bytes / transferred bytes`。

## 5. Shared-Memory Bank Mapping

典型 32-bit word 情况：

\[
bank = word\_index \bmod 32
\]

`tile[32][32]` 按列读：stride=32 words → 每个 lane 落同 bank。

`tile[32][33]` 按列读：stride=33 words → `33 mod 32 = 1`，bank 轮转。

## 6. Reduction Complexity

Warp 内 32 个值通过 shuffle-down 归约：

\[
\log_2 32 = 5\ rounds
\]

## 7. Amdahl's Law

如果热点占比为 `p`，该部分加速 `s` 倍：

\[
Speedup = \frac{1}{(1-p)+p/s}
\]

它解释了为什么先找真正 hot spot 比“优化看起来慢的 kernel”更重要。

## 8. 数据复用与 Tile 的 Trade-off

Tile 增大通常：

```text
reuse ↑
Arithmetic Intensity ↑
register/shared footprint ↑
resident blocks ↓
pipeline/epilogue complexity ↑
```

因此 tile size 是受约束优化问题，而不是“越大越好”。
