# 核心公式速查

| 主题 | 公式/关系 |
|---|---|
| CPU 时间 | `CPU Time = Instruction Count × CPI × Clock Cycle = IC × CPI / Frequency` |
| IPC/CPI | `IPC = Instructions / Cycles`；`CPI = Cycles / Instructions` |
| AMAT | `AMAT = Hit Time + Miss Rate × Miss Penalty` |
| Cache 集合数 | `Sets = Cache Capacity / (Line Size × Associativity)` |
| Cache Offset | `Offset bits = log2(Line Size)` |
| 补码范围 | `[-2^(n-1), 2^(n-1)-1]` |
| IEEE 754 Normal | `(-1)^s × (1.f) × 2^(E-bias)` |
| 写放大 | `WA = NAND Physical Writes / Host Logical Writes` |
| TLB Reach | 近似 `Entries × Page Size` |
