# PDF → Repository 内容映射

PDF 是一次冻结的 Professional Edition；GitHub Markdown 是在其基础上演化的 V2 教材源。两者不是逐字同步关系。

## 1. 主要映射

| PDF 内容 | Repository |
|---|---|
| 封面 / 项目定位 | `README.md` |
| 使用说明 | `docs/00-preface.md` |
| Knowledge Map | `docs/knowledge-map.md` |
| 100 题索引 | `docs/100-question-index.md` |
| Q001–Q100 题干 | `questions/**/qXXX-*.md` |
| 基础答案 / 推导 | 每题 `30 秒版本` + `标准推导` |
| 追问 | 每题 `追问树` |
| 高频错误 | 每题 `高频错误` |
| 面试表达 | 每题 `30 秒版本` + `3 分钟专业回答模板` |
| 学习路线 | `docs/learning-path.md` |
| 官方题型范围依据 | `references/official-sources.md` |
| 原始 PDF | `book/剑指QuantOffer_金融量化算法岗100题_专业版.pdf` |

## 2. V2 Markdown 比 PDF 多了什么

每道题新增或系统强化：

- Formalization：变量、假设、数学对象；
- Why：方法成立的结构性原因；
- 量化金融 / 工程语境；
- 题目特定的模型风险和失效场景；
- 追问的**回答方向**，而不只是问题列表；
- OOS / simulation / replay / parity 等验证思路；
- 关联题和教材阅读；
- 明确的来源与内容边界。

## 3. 内容边界

为了避免“扩写后看不出哪些来自原 PDF”，每题最后都有：

- **PDF 来源内容**：题干、基础答案、初始推导/追问/错误/表达；
- **V2 扩展内容**：后续专业化分析；
- `source_type`：只表示题目来源口径，不把重构题冒充内部真题。

## 4. 后续同步建议

如果未来发布 PDF V2，建议由 Markdown 作为 source of truth 重新排版生成，而不是手工双向修改 PDF 和 Markdown。这样可以减少内容漂移。
