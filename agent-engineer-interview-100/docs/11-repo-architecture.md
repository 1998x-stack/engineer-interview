# Repository Architecture

> GitHub Edition 扩展：解释题库为什么按“内容源 → Markdown → 校验”组织。

## Source of Truth

```text
data/questions.json
      ↓
100 question Markdown
      ↓
questions/README.md index
      ↓
validation / link checks
```

`data/questions.json` 保存 PDF-derived 核心字段：

- 题目。
- 30 秒回答。
- 深挖点。
- 连续追问。
- 易错回答。
- Know-Why / Know-How。

Expanded Edition 的专业扩展存在各 Qxxx Markdown 中。

## 为什么不把所有内容只存 JSON？

因为专业章节包含：

- Mermaid。
- 长解释。
- 伪代码。
- Trade-off。
- Production Checklist。
- 外部工程资料链接。

这些更适合作为可读 Markdown 维护；JSON 继续充当“原始核心字段契约”。

## CI 质量门

`scripts/validate_repo.py` 当前检查：

1. 恰好 Q001–Q100。
2. 结构化数据字段完整。
3. 每个原始字段仍出现在对应 Markdown。
4. Q100 20 个系统追问完整。
5. Expanded Edition 关键章节完整。
6. 单题内容规模达到专业扩展最低门槛。
7. PDF 存在。

此外：

- `build_index.py --check`：总索引没有漂移。
- `check_links.py`：本地 Markdown/PDF 链接可解析。

## Stable ID

题号 `q001`–`q100` 是稳定 ID：

- 文件名稳定。
- Issue / PR 可直接引用。
- data JSON 可被自动工具消费。
- 未来可生成静态站点、Quiz、Agent interviewer。

标题可以优化，ID 不随意变化。

## 内容修改原则

### 修改 PDF-derived 字段

必须同时修改 `data/questions.json` 与对应 Markdown，并解释理由。

### 修改 Expanded 内容

可直接改 Markdown，但要满足：

- 不覆盖/扭曲原始字段。
- 新的 framework/spec fact 最好加入 `docs/09-references.md`。
- 说明 applicable boundary 和 trade-off。
- 避免只增加术语。

## 未来自动化

推荐后续增加：

- Markdown front matter lint。
- Mermaid syntax validation。
- 外部链接定期检查。
- 随机题库生成。
- Difficulty/frequency 数据分析。
- 静态站点搜索。
- Evals：检查重复模板比例和内容覆盖率。

---

## Expanded Edition 使用提示

阅读任何章节时，优先寻找三个东西：**Invariant、Failure Window、Verification Signal**。如果一个方案只有组件名而没有这三项，它通常还停留在 demo 级。完整方法见 [Expanded Edition 内容设计规范](12-expanded-edition-methodology.md)。
