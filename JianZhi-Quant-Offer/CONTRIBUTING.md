# Contributing

欢迎修正数学推导、补充反例/边界、增强工程验证、添加可核验官方资料或改善站点体验。

## 1. 贡献优先级

高价值 PR 通常属于以下类型：

1. 修正数学/统计错误；
2. 把通用模板段落改成题目特定内容；
3. 为追问补准确的回答方向；
4. 增加 PIT / OOS / replay / numerical stability 等实际风险；
5. 添加可执行示例与测试；
6. 补充官方公开面试/岗位来源。

单纯“把一段写得更长”不是高质量贡献。

## 2. 来源与归因

- 不把匿名论坛传闻包装成“某公司真题”；
- 新增具体公司归因必须给官方公开来源；
- 可添加教材/论文作为延伸阅读，但需与题目直接相关；
- PDF 原始内容与后续扩展应保持边界可见。

## 3. 修改单题

每题应符合 [Question Writing Standard](docs/question-writing-standard.md)。修改后至少自查：

- [ ] 基础答案正确；
- [ ] Formalization 与题目直接相关；
- [ ] 追问回答和追问文本一一对应；
- [ ] 没有无条件化经典定理；
- [ ] Quant context 不构成投资建议；
- [ ] 内部链接没有破坏。

## 4. 提交前 QA

```bash
python scripts/validate_repo.py
```

若安装了文档依赖：

```bash
mkdocs build --strict
```

## 5. Commit 示例

```text
fix(q015): clarify BH dependence assumptions
docs(q039): expand purged walk-forward validation
feat(q094): add L3 state invariants and recovery notes
fix(q085): correct theta-gamma relation notation
docs(index): improve derivatives learning path
```

## 6. Review 标准

Reviewer 应优先检查：

**correctness > provenance > clarity > completeness > style**。

如果内容更漂亮但数学/来源不可靠，不应合并。
