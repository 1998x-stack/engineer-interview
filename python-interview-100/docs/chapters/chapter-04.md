# Chapter 04 - OOP 与 Python Data Model

理解属性访问、descriptor、MRO、super、metaclass 与 __slots__ 等高级机制。

## 仓库增强版：章节深挖

### 深入学习路线

本章是高级 Python 的分水岭。建议围绕 **attribute lookup** 画图：metaclass 创建 class → class dict 中 descriptor → instance lookup → MRO → super。

**源码路线**：`Objects/typeobject.c`、`descrobject.c`、`funcobject.c`。

**组合追问**：Q34→Q35→Q36；Q37→Q38；Q39 与 `__init_subclass__` 的取舍。

## 本章目标

把属性访问看作协议而非“点号语法”。descriptor、MRO、super、metaclass 都是在控制对象模型中的查找与构造流程。

## 题目列表

- [Q31. __new__ 和 __init__ 有什么区别？](../questions/04-oop-data-model/q31.md) - ★★★ / 高
- [Q32. 实例方法、classmethod、staticmethod 如何选择？](../questions/04-oop-data-model/q32.md) - ★★ / 极高
- [Q33. Python 的“private”是怎么实现的？](../questions/04-oop-data-model/q33.md) - ★★ / 高
- [Q34. __getattribute__ 和 __getattr__ 有什么区别？](../questions/04-oop-data-model/q34.md) - ★★★★ / 高
- [Q35. 什么是 descriptor？为什么它如此重要？](../questions/04-oop-data-model/q35.md) - ★★★★★ / 高
- [Q36. property 是如何工作的？](../questions/04-oop-data-model/q36.md) - ★★★ / 高
- [Q37. MRO 是什么？C3 linearization 解决什么问题？](../questions/04-oop-data-model/q37.md) - ★★★★ / 高
- [Q38. super() 为什么不是“调用父类”？](../questions/04-oop-data-model/q38.md) - ★★★★ / 高
- [Q39. 什么是 metaclass？什么时候真的需要？](../questions/04-oop-data-model/q39.md) - ★★★★★ / 中
- [Q40. __slots__ 有什么用？有哪些坑？](../questions/04-oop-data-model/q40.md) - ★★★★ / 高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
