# 八条连续追问链

这些链条来自 PDF 附录 B，并为 GitHub 版增加了对应题号导航。

- **Cache 链**：局部性 → Cache line → Tag/Index/Offset → 相联度 → Miss → 写策略 → MESI → False Sharing
- **Load 链**：Load/Store → VA → TLB → Page Walk → PA → L1/L2/LLC → Memory Controller → DRAM
- **流水线链**：Pipeline → RAW → Forwarding → Load-Use → Branch → Prediction → OoO → Renaming → ROB
- **多核链**：Private Cache → Coherence → MESI → Store Buffer → Memory Ordering → Fence → Atomic
- **虚拟内存链**：VA → MMU → Multi-level Page Table → TLB → TLB Miss → Page Fault → Huge Page → Shootdown
- **DMA 链**：PIO → DMA Descriptor → Device Bus Master → DRAM → Interrupt → Cache Maintenance → IOMMU
- **性能链**：Frequency → CPI/IPC → Frontend → Branch → ILP → Cache/TLB → Memory Wall → Bandwidth
- **程序优化链**：顺序访问 → Spatial Locality → Prefetch → TLB Locality → DRAM → Vectorization → Parallelism
