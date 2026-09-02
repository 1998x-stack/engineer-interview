# 内容来源与版本策略

本仓库将内容分成两层：

1. **PDF 基线**：来自 `assets/pdf/LLM_Inference_Interview_100_2026.pdf`，保留原题的核心回答、公式、场景和追问。
2. **工程扩展**：Markdown 中 `2026 工程扩展`、`专家级深挖`、`源码 / Runtime 视角`、`Benchmark Lab` 等章节，是为 GitHub 版新增的系统化扩展。

对于 vLLM、SGLang、TensorRT-LLM、FlashInfer、量化 backend 等快速演进组件：

- 所有实现结论应绑定版本/commit；
- README 或题目中的“当前支持”不应被理解成永久 API 保证；
- 若官方文档与历史 PDF 冲突，以题目标注的版本边界为准；
- 贡献者更新版本敏感信息时，建议同时更新 `CHANGELOG.md`。
