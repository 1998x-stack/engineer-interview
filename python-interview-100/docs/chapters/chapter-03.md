# Chapter 03 - 函数、闭包与装饰器

把函数当一等对象理解，掌握闭包、late binding、装饰器、缓存与调用签名。

## 仓库增强版：章节深挖

### 深入学习路线

把函数当对象学习：function object → closure cell → descriptor binding → decorator → cache。这样装饰器和闭包不再是语法技巧，而是对象模型的直接结果。

**工具路线**：`inspect.signature`、`__defaults__`、`__closure__`、`__wrapped__`、`functools`。

**组合追问**：Q24+Q25、Q26+Q27+Q28、Q30 与 Q20/Q54 的生命周期问题。

## 本章目标

所有函数机制题都问两个时间点：定义时发生什么、调用时发生什么。闭包、默认参数、装饰器、缓存都能用这个框架统一。

## 题目列表

- [Q21. *args 和 **kwargs 的本质是什么？](../questions/03-functions-closures-decorators/q21.md) - ★ / 极高
- [Q22. positional-only 与 keyword-only 参数解决什么问题？](../questions/03-functions-closures-decorators/q22.md) - ★★ / 中
- [Q23. 为什么说函数是一等对象？](../questions/03-functions-closures-decorators/q23.md) - ★ / 高
- [Q24. 什么是闭包？](../questions/03-functions-closures-decorators/q24.md) - ★★ / 极高
- [Q25. late binding closure 为什么会得到 [2,2,2]？](../questions/03-functions-closures-decorators/q25.md) - ★★★ / 极高
- [Q26. 装饰器本质是什么？](../questions/03-functions-closures-decorators/q26.md) - ★★ / 极高
- [Q27. 为什么 decorator 通常需要 functools.wraps？](../questions/03-functions-closures-decorators/q27.md) - ★★ / 高
- [Q28. 如何实现带参数装饰器？](../questions/03-functions-closures-decorators/q28.md) - ★★ / 高
- [Q29. lambda 与普通 def 的区别是什么？](../questions/03-functions-closures-decorators/q29.md) - ★ / 中
- [Q30. functools.lru_cache 有哪些工程陷阱？](../questions/03-functions-closures-decorators/q30.md) - ★★★ / 高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
