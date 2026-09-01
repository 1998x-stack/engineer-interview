# Contributing

本仓库强调“可解释的面试推理”，而不是只追加 AC 代码。

## 新增/修改题目的最低要求

1. 每题一个 Markdown，编号不可复用。
2. Front Matter 必须包含 `id / leetcode / difficulty / priority / evidence / pattern / category`。
3. 必须写清：暴力基线、关键观察/不变量、复杂度、边界测试、至少两个追问。
4. Python 解法必须能通过 `ast.parse` 语法检查；复杂题尽量补充单元测试。
5. “Reported / R” 只能用于有可公开访问面经证据的题；个人面经不能描述为公司官方题库。
6. 不复制 LeetCode 或书籍的完整题面；只保留原创概括、算法分析和必要链接。

提交前运行：

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```


## 内容质量标准

提交题目内容前请阅读 [`docs/00-guide/problem-authoring-standard.md`](docs/00-guide/problem-authoring-standard.md)。S 级题尤其需要多解法比较、正确性说明、bug 定向测试和工程化追问。
