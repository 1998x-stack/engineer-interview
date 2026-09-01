# Contributing Guide

感谢对 Transformer Interview 100 的贡献。本仓库的目标不是“增加更多字数”，而是增加 **正确、可验证、可迁移的技术密度**。

## 1. 修改题目的基本规则

### 保持稳定编号

- Q001–Q100 不因插题整体重排；
- 新主题优先放入扩展页/System Design/未来版本；
- 修改标题时同步 `data/questions.json`、索引与 MkDocs 导航。

### PDF Core 不静默改写

`PDF Core` 是参考 PDF 的基线层。

如果必须修正：

1. 明确写出原结论；
2. 说明为何需要更正；
3. 给出可靠依据；
4. 不把模型知识或个人经验伪装成 PDF 原文。

### Professional Expansion 可扩展

但要明确区分：

- 论文直接支持的事实；
- 工程经验；
- 推导/推断；
- 需要 benchmark 才能确定的性能结论。

## 2. 一道高质量题页应包含什么

至少覆盖：

- **Definition**：输入/输出/目的；
- **Formula & Shape**：关键 tensor 轴；
- **Why**：旧方案瓶颈；
- **Cost**：params/FLOPs/memory/IO/communication；
- **Gotcha**：一个真实实现坑；
- **Boundary**：何时结论不成立；
- **Verify**：单测/ablation/profiler；
- **Follow-up**：至少两层追问。

## 3. 公式与数学规范

- 每个新符号第一次出现要解释；
- 不只写 $O(T^2)$，说明忽略了哪些维度；
- 参数量和 FLOPs 不混为一谈；
- `train / prefill / decode` 成本不同的题必须拆开；
- 数值例子注明 byte/GiB 单位。

## 4. 性能结论规范

禁止无条件：

> “X 一定更快。”

推荐：

> “在 batch=..., T=..., dtype=..., GPU=... 的设置下，瓶颈主要是...；需要 profiler 验证。”

至少给：

- hardware；
- batch/context；
- dtype；
- baseline；
- correctness/quality parity。

## 5. Coding 规范

任何优化代码先有 reference/oracle。

推荐测试：

- causal future leakage；
- padding invariance；
- full-vs-cache logits；
- finite softmax；
- GQA head mapping；
- tiny overfit。

避免在文档中只给无法运行、没有 shape contract 的“大段伪代码”。

## 6. 引用规范

优先：

1. 原论文；
2. 官方文档；
3. 高质量技术报告。

不要用二手博客替代可以直接引用的原论文来支持核心算法事实。

## 7. Writing Style

- 先结论，后推导；
- 短段落 + 明确小标题；
- 中英文术语首次出现可并列；
- 不堆“本质上/显著/极大”等无量化形容词；
- 不使用“永远”“必然”“全面优于”等没有条件的结论。

## 8. 提交前检查

```bash
python scripts/check_docs.py
python scripts/check_links.py
pytest -q
```

若本地已安装 MkDocs：

```bash
mkdocs build --strict
```

## 9. PR 应回答的三个问题

1. **What changed?**
2. **What evidence supports it?**
3. **How can a reviewer verify it?**

若无法回答第 3 个问题，通常说明内容还不够工程化。
