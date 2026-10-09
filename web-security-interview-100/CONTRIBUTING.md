# Contributing

欢迎补充题解、标准映射、工程案例与勘误。

## 原则

1. **优先根因**：不要只堆漏洞名或 Payload。
2. **区分来源**：PDF 母版内容与新增研究/工程经验必须明确区分。
3. **可验证**：新增防御建议尽量转成 Security Invariant、代码审计点或测试项。
4. **引用一手资料**：优先 OWASP、IETF/RFC、CWE/MITRE、框架/浏览器官方文档。
5. **防御性**：不提交针对真实目标的破坏性操作链、绕过指引或隐藏痕迹的方法。
6. **版本明确**：会变化的标准/框架行为应写版本或日期。

## 修改单题

使用 `templates/question-template.md` 的结构。保持：

- `id: Qxxx`
- 一题一文件
- 不改变原题号
- 新增内容放在“GitHub 增强版”
- 更新关联题目与参考资料

提交前运行：

```bash
python scripts/validate_repo.py
```
