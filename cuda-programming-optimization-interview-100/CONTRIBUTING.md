# Contributing

## 题解修改原则

1. 先保证技术正确，再追求“面试表达漂亮”。
2. 架构特定结论必须写明目标 GPU / compute capability。
3. 性能结论尽量附 benchmark 条件或 Nsight 指标，不写“永远更快”。
4. 新增外部事实时优先引用 NVIDIA 官方 CUDA / Nsight / CUTLASS / PTX 文档。
5. 不把匿名面经中的答案当技术权威；面经只用于说明题型来源。

## Markdown 结构

每题建议保持：PDF 基线题解 → 深入分析 → 性能因果链 → 架构视角 → 面试回答 → 实战验证 → Rubric → 自测 → 参考资料。

## Pull Request Checklist

- [ ] `python scripts/validate_repo.py` 通过
- [ ] 没有破坏题号/章节索引
- [ ] 新增代码可编译或明确标注为伪代码
- [ ] 性能结论包含适用条件
- [ ] 外部链接指向稳定/权威资料
