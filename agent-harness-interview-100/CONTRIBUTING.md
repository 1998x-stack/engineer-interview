# Contributing

## 新增/修改题目的原则

1. 不把无法验证的内部题标成“某厂真题”。
2. 先写 Know-Why，再写 How；框架/API 只是例子，不是答案本身。
3. 每个新机制必须对应至少一个 failure mode 和一个可验证 metric/eval。
4. 版本相关内容优先引用官方一手资料，并注明访问日期或版本。
5. 不复制第三方图书大段原文；引用只保留必要信息并链接来源。

## Markdown 质量门槛

每题必须包含：front matter、结论、Why、How、Failure Modes、Trade-offs、Eval、追问、90 秒回答、5 分钟回答、扩展阅读、关联题。

提交前运行 `python scripts/validate_repo.py`。

## v1.1 内容贡献 Checklist

提交某一道题的增强前，请确认：

- [ ] 新内容明确属于 Source / Teaching / Engineering Research 哪一层；
- [ ] 至少补强一个具体 failure mode，而非泛泛增加段落；
- [ ] 至少给一个可序列化 schema、状态转移或明确 API contract；
- [ ] 至少给一个 fault-injection / adversarial test；
- [ ] 至少给一个可证伪 eval / ablation；
- [ ] 指标能反映质量与系统代价，而不只看 solve-rate；
- [ ] 新增外部事实优先引用官方文档/论文；
- [ ] `python scripts/validate_repo.py` 通过。
