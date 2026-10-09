# 附录 C · 高中数学竞赛教练面试作品集指南

作品集的任务不是“显得很努力”，而是提供一组可验证证据，证明你具备：

$$
\text{Solve}\rightarrow\text{Explain}\rightarrow\text{Teach}\rightarrow\text{Build}.
$$

## 1. 推荐目录

```text
portfolio/
├── 00-index.pdf
├── 01-teaching-philosophy.pdf
├── 02-math-samples/
│   ├── olympiad-solution-01.pdf
│   └── proof-critique-01.pdf
├── 03-topic-handout/
│   ├── handout.pdf
│   └── change-log.md
├── 04-demo-lesson/
│   ├── lesson-plan.md
│   ├── board-plan.png
│   ├── hint-ladder.md
│   └── exit-ticket.md
├── 05-assessment/
│   ├── blueprint.md
│   └── rubric.md
├── 06-student-diagnosis/
│   ├── anonymized-data.csv
│   ├── diagnosis.md
│   └── intervention-plan.md
└── 07-problem-bank/
    ├── schema.yml
    └── sample-20.csv
```

## 2. 首页 Index 要解决什么

面试官通常没有时间逐页翻。首页应在 30 秒内回答：

- 你是谁 / 目标岗位；
- 你的四个最强证据是什么；
- 每个证据在哪一页/哪个链接；
- 是否有可点击目录。

不要把简历完整复制一遍。

## 3. 数学能力样例

建议放 2–3 份，而不是 20 份：

1. 一份完整竞赛证明，体现严谨性；
2. 一份同题多解，体现方法比较；
3. 一份 proof critique，体现审查与教学能力。

每份旁边写 3 行注释：核心结构、为什么选这题、它证明了你什么能力。

## 4. 专题讲义

建议 10–20 页，结构至少包括：

```text
学习目标
→ prerequisite
→ 核心母式/定理及条件
→ 母题
→ 方法抽象
→ 对比题/错误题
→ 三层变式
→ 课末检查
→ 一周后复测
```

### 加分证据：版本迭代

保留 `v1 → v2` 的修改说明，例如：

> “原 Q4 独立完成率只有 15%，且大多数学生卡在未学过的辅助 lemma，因此 v2 将其后移，并新增一题过渡题。”

这比“讲义排版很漂亮”更能证明教研能力。

## 5. 试讲材料

除了 lesson plan，再附：

- 分钟级时间轴；
- 板书地图；
- 学生可能错误；
- 三级提示；
- exit ticket；
- 如果有录像，提供 3–5 分钟精剪片段或时间戳索引。

## 6. 学情诊断案例

必须匿名化。建议格式：

| 项目 | 内容 |
|---|---|
| 目标 | 例如 8 周提升联赛二试几何基础得分能力 |
| 证据 | 3 次测评、作业行为、提示层级 |
| 诊断 | 区分知识、识别、证明、速度问题 |
| 干预 | 具体题型/频次/提示策略 |
| 指标 | 近迁移正确率、首步成功率、证明得分 |
| 复盘 | 哪项改善、哪项没有、下一步 |

如果没有真实学生数据，可以明确写“模拟案例”，不要伪造成真实带队成果。

## 7. 题库样例

20 题足够，但元数据必须专业：

```yaml
id: GEO-INV-001
domain: geometry
subtopics: [inversion, power-of-point]
difficulty: 4
expected_time: 40m
prerequisites: [cyclic, power-of-point]
core_idea: invert at common point
common_errors: [wrong image, missing tangency]
hint_level_1: ...
hint_level_2: ...
```

## 8. 不要放什么

- 大量无说明的获奖证书扫描件；
- 学生姓名、学校、联系方式等可识别信息；
- 只有答案没有教学说明的几十页题解；
- 无法证明属于自己的机构内部资料；
- 过度装饰、打开慢、面试现场无法快速定位的文件。

## 9. 最终自检

- [ ] 30 秒能打开任何一份核心作品；
- [ ] 每个 artifact 都对应一个岗位能力；
- [ ] 所有学生数据匿名化；
- [ ] 所有成果描述可核验、不过度归因；
- [ ] 有至少一个“根据反馈修改过”的作品；
- [ ] PDF、链接和本地备份均可用。
