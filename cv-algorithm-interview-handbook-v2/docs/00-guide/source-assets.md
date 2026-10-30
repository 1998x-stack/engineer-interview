# 原始资料、授权与可复现性说明

## 源码仓库中实际提供了什么

本模块可追踪的内容包括 100 道 Markdown 题解、JSON/CSV 元数据、MkDocs 配置和示例代码。

README 早期列出的原始 PDF 路径为：

- `assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf`
- `docs/assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf`

**2026-10-30 检查的 main Git 树没有这两份 PDF。** 因此 README/网站不再提供无法兑现的下载链接；本仓库不能声称干净克隆可读取 PDF 或证明与 PDF 逐页一致。请不要将未获明确授权的 PDF 上传到公共仓库。

若拥有合法可分发的原始资料，可在本地放置到上述路径，然后使用：

```bash
python scripts/validate_repo.py --require-pdf
```

普通贡献者运行 `python scripts/validate_repo.py` 时，源文件不存在不会阻止题库文档质量检查；脚本会发出明确提示。MkDocs 网站只包含可追踪的 Markdown、公式和代码内容。

## 参考资料与事实核对

- [经典论文与公开依据](../12-references/papers.md)
- [100 道题索引](../11-cheatsheets/top30.md)
- [手撕代码及测试约定](../11-cheatsheets/coding-drills.md)

论文与公开技术资料用于验证方法定义；面经来源不应被解释为公司官方题库。代码的实际结果需要通过单元测试与独立 oracle 比较验证，性能数字需要注明硬件及运行配置。

## 验收范围

`python scripts/validate_repo.py` 检查的是题号、frontmatter、JSON/CSV 对应关系、要求的章节结构和本地 Markdown 链接，不会自动判断所有技术结论是否科学正确。算法相关题解应补充可运行示例与客观数值测试；版权和资料真实性仍需人工复核。
