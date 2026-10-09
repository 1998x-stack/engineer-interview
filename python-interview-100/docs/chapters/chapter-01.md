# Chapter 01 - Python 基础语义与对象模型

建立 Python 的正确心智模型：名字绑定、对象身份、可变性、作用域和调用语义。

## 仓库增强版：章节深挖

### 深入学习路线

本章建议沿 **名字绑定 → 求值顺序 → 可变性 → 作用域 → 函数调用** 递进。不要孤立背 `is`、`None`、默认参数；它们本质上都可以从“对象何时创建、名字何时绑定、表达式何时求值”推导。

**源码/工具路线**：`dis` → `inspect` → Execution Model → Data Model → `Python/compile.c` / `Python/ceval.c`。

**组合追问**：Q03+Q04+Q05、Q07+Q08、Q09+Q10。面试官常通过一个短代码片段把多个语义点串起来。

## 本章目标

把“名字绑定、对象身份、对象状态、求值时机”四条线分开。遇到反直觉代码，先画名字到对象的引用关系，再判断操作是原地修改还是重新绑定。

## 题目列表

- [Q01. Python 是解释型语言还是编译型语言？](../questions/01-python-semantics/q01.md) - ★★ / 高
- [Q02. is 和 == 有什么区别？](../questions/01-python-semantics/q02.md) - ★ / 高
- [Q03. Python 变量保存的是值还是对象？](../questions/01-python-semantics/q03.md) - ★★ / 高
- [Q04. Python 是 pass-by-value 还是 pass-by-reference？](../questions/01-python-semantics/q04.md) - ★★ / 高
- [Q05. mutable 和 immutable 的本质区别是什么？](../questions/01-python-semantics/q05.md) - ★★ / 高
- [Q06. None 到底是什么？为什么推荐 is None？](../questions/01-python-semantics/q06.md) - ★ / 高
- [Q07. Python 的 truthy / falsy 规则是什么？](../questions/01-python-semantics/q07.md) - ★★ / 高
- [Q08. and / or 为什么不一定返回 bool？](../questions/01-python-semantics/q08.md) - ★★ / 中
- [Q09. 为什么 mutable default argument 是经典陷阱？](../questions/01-python-semantics/q09.md) - ★★ / 极高
- [Q10. global 和 nonlocal 有什么区别？LEGB 如何工作？](../questions/01-python-semantics/q10.md) - ★★ / 高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
