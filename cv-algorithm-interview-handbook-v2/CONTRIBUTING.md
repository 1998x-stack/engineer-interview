# Contributing

欢迎补充题解、勘误、公开面经依据和工程案例。为了保持 100+ 题长期可维护，请遵守以下规范。

## 问题页结构

每个 `qXXX.md` 至少包含：

- YAML front matter（id/title/chapter/difficulty/frequency/tags/source_label）；
- 30 秒回答；
- 2–5 分钟标准回答；
- 关键公式/信息流（适用时）；
- 高频追问与参考答案；
- 常见失分点；
- V2 专业深化；
- 工程/项目视角；
- 自测与关联题。

## 内容质量

- 区分**公开面经原题/近似题**与**通用知识扩展**；
- 公式需解释变量、shape 和约定；
- 性能数字必须说明硬件/precision/batch/输入；
- 比较方法时尽量说明 control variables，不做绝对化结论；
- 不复制受版权保护的长段落。

## 提交前检查

```bash
python scripts/validate_repo.py
```

如修改导航，再运行：

```bash
pip install -r requirements-docs.txt
mkdocs build --strict
```
