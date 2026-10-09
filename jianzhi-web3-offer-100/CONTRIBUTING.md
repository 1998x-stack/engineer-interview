# Contributing

本仓库适合以“题号”为最小变更单元维护。提交内容修正时，请遵循以下规则：

1. 在 PR 标题中标记题号，例如 `[Q69] clarify ERC-4337 / EIP-7702 relation`。
2. 协议事实优先引用 EIP/ERC、官方协议文档、官方 whitepaper 或官方代码文档。
3. 对随版本变化的内容注明版本或核验日期，不把当前实现写成永恒事实。
4. 不直接删除 PDF 主干内容；若发现原内容需要修正，应在变更说明中明确“原表述 -> 新表述 -> 依据”。
5. 安全题尽量补充：资产、攻击前提、影响、PoC 思路、mitigation、regression test。
6. 系统设计题尽量补充：状态机、幂等、reorg/finality、SLO/监控、灾备与信任边界。
7. 如果修改了 `data/questions.json` 中的题目主干或希望重建专业深化层，先运行：

```bash
python scripts/enrich_questions.py
```

8. 修改完成后运行：

```bash
python scripts/validate_repo.py
```

## 内容层级

- **PDF 主干**：与书中结构化源一致的核心答案。
- **GitHub 扩展**：工程化补充、测试、白板图、版本化资料。
- **v2 专业深化**：通用工程知识与推导；必须保持显式标签，不能与 PDF 原文混淆。

如果二者发生冲突，应优先修正技术事实，同时在 CHANGELOG 中记录原因。
