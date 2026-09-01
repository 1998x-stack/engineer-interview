# 栈、解析器与单调结构

**核心能力：** Stack / Parser / Monotonic Structure






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：延迟结算与嵌套状态**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- stack 里到底存什么
- 何时出栈就意味着答案可确定
- parser 区分 token 层与语义层

## 本章完成标准

- [ ] S 级题全部做到无提示手写；
- [ ] 每题都能先说基线，不依赖“见过原题”；
- [ ] 每个 pattern 至少能给出一个反例说明错误做法为什么错；
- [ ] 能比较至少两种方案的时间、空间和工程 trade-off；
- [ ] 随机抽一题，90 秒内完成口述推导；
- [ ] 至少挑两题继续回答 streaming / sharding / memory-bound 追问。

## 推荐复习方式

第一次按题号顺序建立模式；第二次只看标题随机做；第三次按 pattern 跨章节混刷。真正的“掌握”标志是约束稍改后仍能重新推导，而不是记得某一份代码。

<!-- CHAPTER-ENRICHMENT-V2:END -->

| # | LC | 题目 | 难度 | 优先级 | 模式 |
|---:|---:|---|---|---|---|
| 031 | 20 | [有效的括号](./031-valid-parentheses.md) | Easy | S | Stack Matching |
| 032 | 155 | [最小栈](./032-min-stack.md) | Medium | S | Augmented State |
| 033 | 394 | [字符串解码](./033-decode-string.md) | Medium | S | Stack Parser |
| 034 | 739 | [每日温度](./034-daily-temperatures.md) | Medium | S | Monotonic Stack |
| 035 | 84 | [柱状图中最大的矩形](./035-largest-rectangle-in-histogram.md) | Hard | S | Monotonic Increasing Stack |
| 036 | 224 | [基本计算器](./036-basic-calculator.md) | Hard | A | Expression Parsing |
