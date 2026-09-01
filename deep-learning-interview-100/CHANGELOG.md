# Changelog

## v2-deep · 2026-09-01

- 逐题增强 Q001–Q100：新增“90 分深挖”，覆盖机制、定量抓手、工程实验、失败边界和白板专项练习。
- 将通用 PyTorch 验证占位替换为题目特定验证协议；保留已有 reference implementation。
- 每题新增“项目化证据链”：建议指标、实验原则、停止条件和 5 分钟深挖路线。
- LoRA 补充现代 PEFT 初始化/缩放视角；FSDP 补充 FSDP2 / DTensor `fully_shard` 语义。
- CI 升级为内容深度检查：最低正文长度、v2-deep 元数据、专属验证协议、必需章节和内部链接。
- 新增 `docs/content-quality.md`，定义 repo 级内容 Review 标准。


## 2026-09-01

- 初始化 100 道独立 Markdown 题库。
- 从 73 页 PDF 完整映射正文与附录内容。
- 新增数学/shape、PyTorch 验证、工程诊断、关联题目和参考资料。
- 新增 Top 30、连续追问链、7/14/30 天训练计划与回答评分标准。
- 新增 CI 结构校验和 MkDocs 配置。
