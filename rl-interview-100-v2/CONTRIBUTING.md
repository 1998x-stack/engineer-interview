# Contributing

## 推荐 PR 类型

1. 修正公式/符号/shape；
2. 增加 primary paper 或官方实现链接；
3. 增补真实工程 failure mode，但必须给出可验证现象；
4. 新增公开面经母题时，请注明“公开母题”还是“扩展追问”；
5. 改代码时同时更新对应问题 Markdown。

## 题目 Markdown 约定

- 不删除“PDF 原始要点”层；
- 新知识写在“Repo 扩展解析”；
- 不把个人经验写成普遍定理；
- 对 2025-2026 LLM-RL 前沿算法优先引用原论文/官方资料；
- 代码必须明确 tensor shape、mask 和 stop-gradient 边界。

提交前运行：

```bash
python scripts/validate_repo.py
```
