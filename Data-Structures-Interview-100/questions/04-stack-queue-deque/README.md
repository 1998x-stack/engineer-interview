# Stack / Queue / Deque

> 本章覆盖 **034-043**，共 10 题。

## 源书稿章节导语

> 嵌套结构、最近未完成状态、单调关系、FIFO 层级搜索。

## 章节能力目标

- Stack 处理“最近未完成状态/嵌套”，Queue 处理 FIFO/BFS，Deque 常用于双端淘汰和单调候选。

## 深化版章节训练目标

**章节核心：** 未完成状态、嵌套与延迟结算

**主要 Pattern：** `Stack / Monotonic Stack / Parser / Queue Amortization`

### 面试前的三次检查

1. 先定义栈中保存什么
2. 证明 pop 后状态责任完成
3. 解析题区分 token 与 grammar

### 难度分布

- `E`：2 题
- `E/M`：1 题
- `H`：2 题
- `M`：5 题

### 推荐训练顺序

1. **基础结构题**：先练接口与基本不变量，不追求花哨优化。
2. **Pattern 题**：把同一结构的 2–3 题连续做，找共同状态定义。
3. **Hard/变体题**：只看约束，不看题名，练从 baseline 推 structure。
4. **Follow-up 复盘**：不重写整题，只回答“哪个前提变了、哪一层结构要换”。

> 章节 README 只负责能力地图；真正的证明、代码审查与对抗测试都在各 `Qxxx.md` 的 §12 专业深化中。

## 题目列表

| ID | 题目 | 难度 | 核心 |
|---|---|---|---|
| Q034 | [有效括号](Q034-有效括号.md) | E | Stack / 字符串 |
| Q035 | [Min Stack](Q035-Min-Stack.md) | M | Stack / 设计 |
| Q036 | [两个栈实现队列](Q036-两个栈实现队列.md) | E/M | Stack / Queue |
| Q037 | [一个/两个队列实现栈](Q037-一个-两个队列实现栈.md) | E | Queue / Stack |
| Q038 | [每日温度：下一个更高温度](Q038-每日温度-下一个更高温度.md) | M | 单调栈 / 数组 |
| Q039 | [Next Greater Element 通用模板](Q039-Next-Greater-Element-通用模板.md) | M | 单调栈 |
| Q040 | [柱状图最大矩形](Q040-柱状图最大矩形.md) | H | 单调栈 / 数组 |
| Q041 | [Decode String：解码嵌套重复串](Q041-Decode-String-解码嵌套重复串.md) | M | Stack / 递归下降 |
| Q042 | [碰撞模拟：Asteroid Collision](Q042-碰撞模拟-Asteroid-Collision.md) | M | Stack / 模拟 |
| Q043 | [Basic Calculator：表达式求值](Q043-Basic-Calculator-表达式求值.md) | H | Stack / Parser |
