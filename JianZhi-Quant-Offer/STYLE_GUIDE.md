# STYLE GUIDE

## 1. 单题结构

所有 `qXXX-*.md` 采用 V2 14 段结构，完整标准见 [docs/question-writing-standard.md](docs/question-writing-standard.md)。

核心顺序：

> **题目 → 考点 → 30 秒结论 → Formalization → 推导 → Why → Quant Context → Failure Modes → Follow-ups → Errors → 3 分钟表达 → 自测 → 关联 → 来源**

## 2. 写作原则

### 先定义，再计算

不要从公式开始。先说明变量、状态、信息集、约束和时间语义。

### 先模型内结论，再现实解释

明确区分：

- theorem / exact result；
- asymptotic approximation；
- empirical regularity；
- engineering heuristic。

### 公式必须有人话解释

每个重要公式后至少回答：

> 它在描述什么？为什么结构是这样？哪个假设最重要？

### 研究题必须能被证伪

出现 prediction/backtest/alpha/ML 时，必须给 OOS、ablation、placebo、sensitivity、replay 等至少一种验证方式。

### 工程题必须写 failure modes

不能只写 happy path。至少考虑：duplicate、out-of-order、gap、null、overflow、stale data、recovery 或数值稳定性中的相关项。

## 3. 语言风格

- 中文为主，保留行业通用英文术语；
- 首次出现的重要英文概念应能从上下文理解；
- 避免“显然”“肯定”“永远”等无条件措辞；
- 不把经验规律写成定律；
- 不写投资建议或收益承诺。

## 4. LaTeX

- 行内公式使用 `$...$`；
- 长推导可使用块级公式；
- 反斜杠必须正确转义，提交前运行 validator，避免 `\alpha` 等被脚本控制字符破坏；
- 同一题符号保持一致。

## 5. 代码与伪代码

- 优先给最小正确实现；
- 明确 time/space complexity；
- production 相关代码补 state invariant / failure handling；
- 示例代码不是交易策略建议。

## 6. 链接与引用

- 内部链接使用相对路径；
- 公司能力归因只链接官方公开来源；
- 教材/论文推荐应与该题确实相关，而不是统一堆参考书。
