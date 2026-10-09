# Contributing

## 新增或修改题目

1. 一个问题只放在一个 Markdown 文件中。
2. 保留 YAML front matter：`id/title/chapter/difficulty/roles/framework/pdf_page/status`。
3. 修改 PDF baseline 时必须说明来源；新增扩展内容放在“扩展解析”中。
4. 不提交针对真实目标的利用 payload、绕过检测、隐藏持久化或未授权访问步骤。
5. 每个新结论尽量链接官方标准/厂商文档/论文。
6. 提交前运行 `python scripts/verify_repo.py`。

## 写作标准

- 先给定义和安全边界，再讲技术细节。
- 明确“根治”与“纵深防御”。
- 场景题必须包含证据、业务影响、控制、验证。
- 避免绝对化表述；注明依赖版本、架构和配置的边界。
