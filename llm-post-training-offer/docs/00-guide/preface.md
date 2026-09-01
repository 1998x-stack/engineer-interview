# 序言：不要背 100 个答案，要建立推理链

2026 年的大模型后训练面试已经从单纯的 RLHF / DPO 概念题，进入“算法 + 数据 + reward + distributed system + Agent environment”的联合考察。

仓库采用《剑指 Offer》式的学习思路：**题目 -> 思路 -> 解法 -> 追问 -> 举一反三**，但内容完全围绕 LLM Post-Training。

每道题最终都应能放回这条回答主线：

```text
Problem -> Objective -> Data -> Reward -> Exploration -> Credit Assignment
        -> Compute/System -> Failure Mode -> Algorithm Choice -> Eval
```

公开面经属于候选人自述，不是企业官方题库。本仓库把可核对到公开面经的问题标为“公开真题”，其余用于覆盖真实面试中的连续追问。
