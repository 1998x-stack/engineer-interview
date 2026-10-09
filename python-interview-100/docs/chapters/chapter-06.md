# Chapter 06 - CPython、内存、GC 与 Import

区分语言规范与 CPython 实现，理解引用计数、循环 GC、分配器与导入系统。

## 仓库增强版：章节深挖

### 深入学习路线

把“内存”拆成五层：引用关系 → cyclic GC → Python allocator → native heap → OS RSS；把“import”拆成 spec/finder/loader → module cache → module execution。

**工具路线**：`gc`、`weakref`、`tracemalloc`、`sys.modules`、`importlib`。

**组合追问**：Q51-Q56 常被合成一条内存排障题；Q57-Q60 常被合成启动与模块系统题。

## 本章目标

先声明“以下是 CPython 实现细节”。对象生命周期、GC、RSS、import cache 都不能用语言规范层面的结论偷换。

## 题目列表

- [Q51. CPython 如何管理对象生命周期？](../questions/06-cpython-memory-import/q51.md) - ★★★★ / 极高
- [Q52. del x 是否等于删除对象？](../questions/06-cpython-memory-import/q52.md) - ★★ / 极高
- [Q53. 什么是 reference cycle？循环 GC 为什么需要它？](../questions/06-cpython-memory-import/q53.md) - ★★★ / 高
- [Q54. weakref 适合解决什么问题？](../questions/06-cpython-memory-import/q54.md) - ★★★ / 中
- [Q55. 为什么对象释放后进程 RSS 不一定下降？](../questions/06-cpython-memory-import/q55.md) - ★★★★ / 中
- [Q56. sys.getsizeof 为什么不是对象“总内存”？](../questions/06-cpython-memory-import/q56.md) - ★★ / 高
- [Q57. Python import 的核心流程是什么？](../questions/06-cpython-memory-import/q57.md) - ★★★ / 高
- [Q58. circular import 为什么会产生 partially initialized module？](../questions/06-cpython-memory-import/q58.md) - ★★★ / 极高
- [Q59. .pyc 是什么？什么时候会失效？](../questions/06-cpython-memory-import/q59.md) - ★★ / 中
- [Q60. monkey patching 什么时候有用，为什么危险？](../questions/06-cpython-memory-import/q60.md) - ★★★ / 中

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
