# Chapter 05 - 迭代器、生成器与资源管理

掌握惰性计算、迭代协议、generator delegation 与 context manager。

## 仓库增强版：章节深挖

### 深入学习路线

本章用“暂停/恢复 + 资源作用域”统一理解：iterator 保存遍历状态，generator 保存执行状态，context manager 保存资源状态。

**源码路线**：`Objects/genobject.c`、`Lib/contextlib.py`、iterator protocol。

**组合追问**：Q41/Q42/Q47 解决可消费性；Q43/Q45/Q46 解决 generator 状态机；Q48-Q50 解决 cleanup。

## 本章目标

惰性计算的核心是“状态可以暂停并继续”，资源管理的核心是“所有控制流路径上都能确定性释放”。

## 题目列表

- [Q41. iterable 和 iterator 有什么区别？](../questions/05-iterators-generators-context/q41.md) - ★★ / 极高
- [Q42. iter(x) 实际发生了什么？](../questions/05-iterators-generators-context/q42.md) - ★★★ / 高
- [Q43. generator 与普通函数有什么区别？](../questions/05-iterators-generators-context/q43.md) - ★★ / 极高
- [Q44. 为什么 generator 通常更省内存？](../questions/05-iterators-generators-context/q44.md) - ★★ / 极高
- [Q45. generator.send() 有什么语义？](../questions/05-iterators-generators-context/q45.md) - ★★★★ / 中
- [Q46. yield from 不只是语法糖吗？](../questions/05-iterators-generators-context/q46.md) - ★★★★ / 中
- [Q47. 为什么 generator/iterator 通常只能消费一次？](../questions/05-iterators-generators-context/q47.md) - ★★ / 高
- [Q48. context manager 的核心协议是什么？](../questions/05-iterators-generators-context/q48.md) - ★★ / 极高
- [Q49. with 为什么比手写 try/finally 更好？](../questions/05-iterators-generators-context/q49.md) - ★★ / 高
- [Q50. contextlib.contextmanager 是如何把 generator 变成上下文管理器的？](../questions/05-iterators-generators-context/q50.md) - ★★★ / 中

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
