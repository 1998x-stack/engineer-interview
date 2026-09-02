# V2 Professional Expansion Report

## Scope

V2 对仓库的目标不是简单扩字，而是把每一道题从“复习提纲”升级成可独立学习、可口述、可实验验证的面试知识单元。

## Question-level changes

Q001–Q100 全部新增 `V2 专业深化`，包含：

1. **更精确的技术表述**：题目专属的公式口径、实现细节、复杂度或边界条件；
2. **回答前提**：要求显式声明 shape、坐标、训练/推理、评测口径等；
3. **机制推理链**：现象 → 数学/信息流 → 机制 → 收益 → 代价 → 失败模式 → 验证；
4. **工程诊断矩阵**：观察现象、优先怀疑项、最小验证实验；
5. **最小消融模板**：control、slice、cost、regression、repeatability；
6. **专家级追问**：把普通追问推向反例、边界和工程后果；
7. **面试表达模板**：把技术事实组织成 3–5 分钟专业回答。

## Repository-level changes

- 10 个章节 README 增加课程定位、学习目标、推荐刷题顺序、Top30 与章节自检；
- `00-guide/` 重写为技术题/项目题/系统题统一回答方法、项目证据卡和 mock interview rubric；
- `11-cheatsheets/` 扩展公式、IoU/NMS/BN 手撕、项目拷问 30 题和 30 天路线；
- 经典论文页补充论文阅读方法；
- `questions.json` / `questions.csv` 增加 `content_version=v2-professional-expanded`；
- `CONTRIBUTING.md` 增加内容质量规范与发布前检查。

## Quality gates

当前自动校验覆盖：

- Q001–Q100 共 100 个问题页；
- 编号连续且 YAML `id` 一致；
- 每题包含 30 秒回答与高频追问；
- 每题包含 V2 专业深化；
- 相对 Markdown 链接不存在断链；
- JSON 元数据为 100 条；
- 两份 PDF 资产存在。

> MkDocs Python 包在本次构建环境中未预装，因此未执行 `mkdocs build --strict`；仓库仍保留对应 CI/requirements，且本地相对链接校验已通过。
