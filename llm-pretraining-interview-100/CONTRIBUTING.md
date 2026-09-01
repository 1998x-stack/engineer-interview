# Contributing

## 内容 PR 最低要求

1. 明确改的是“源资料支持的事实”还是“工程经验/推断”；
2. 新增技术事实优先引用原始论文或官方文档；
3. 新增面经题型必须给公开可访问来源，并标记为候选人分享而非官方题库；
4. 任何显存/FLOPs 数字必须写假设；
5. 分布式内容必须说明 shard/collective/topology；
6. Debug 建议必须包含验证方法，而不是只给“调 LR”等处方。

## 修改后运行

```bash
python scripts/validate_repo.py
```
