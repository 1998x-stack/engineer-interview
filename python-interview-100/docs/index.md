# Python Interview 100 - 剑指式题解知识库

> Python 3.14 基线 · 100 道核心面试题 · 一题一 Markdown · 可直接发布为 GitHub Pages

这是《Python 面试宝典：100 道核心真题》的 GitHub 仓库化版本。目标不是把 PDF 拆成 100 个文件，而是把它重构成一个 **可搜索、可链接、可执行、可持续维护** 的 Python 面试知识库。

## 仓库特色

- **100 题 = 100 个独立 Markdown**，便于 issue / PR 精确讨论。
- 每题统一包含：题目定位、60 秒回答、四层高分结构、原理拆解、实验、Gotchas、工程检查表、连续追问、自测与官方参考。
- **Python 3.14 版本敏感内容单独标注**，重点覆盖 free-threaded CPython、TaskGroup、InterpreterPoolExecutor 等现代主题。
- 附带原始专业 PDF、Python 示例、MkDocs Material 配置和 GitHub Pages workflow。
- `scripts/validate_repo.py` 自动检查 100 题数量、front matter、必备章节和 PDF 是否齐全。

## PDF

- [Python 面试宝典：100 道核心真题 · 专业版](../book/Python面试宝典_100道核心真题_专业版.pdf)

## 推荐学习方式

1. **第一轮**：只读每题的“30-60 秒标准回答 + Gotchas”。
2. **第二轮**：闭卷口述，并运行 `examples/qXX.*` 中的最小实验。
3. **第三轮**：只看“连续追问”，训练 3-5 层追问能力。
4. **冲刺轮**：使用 [S/A/B 冲刺路线](appendices/study-roadmap.md) 与 [20 条高分原则](appendices/20-golden-rules.md)。

## 10 大模块

### 01. Python 基础语义与对象模型

建立 Python 的正确心智模型：名字绑定、对象身份、可变性、作用域和调用语义。

- [Q01. Python 是解释型语言还是编译型语言？](questions/01-python-semantics/q01.md) - ★★ · 高
- [Q02. is 和 == 有什么区别？](questions/01-python-semantics/q02.md) - ★ · 高
- [Q03. Python 变量保存的是值还是对象？](questions/01-python-semantics/q03.md) - ★★ · 高
- [Q04. Python 是 pass-by-value 还是 pass-by-reference？](questions/01-python-semantics/q04.md) - ★★ · 高
- [Q05. mutable 和 immutable 的本质区别是什么？](questions/01-python-semantics/q05.md) - ★★ · 高
- [Q06. None 到底是什么？为什么推荐 is None？](questions/01-python-semantics/q06.md) - ★ · 高
- [Q07. Python 的 truthy / falsy 规则是什么？](questions/01-python-semantics/q07.md) - ★★ · 高
- [Q08. and / or 为什么不一定返回 bool？](questions/01-python-semantics/q08.md) - ★★ · 中
- [Q09. 为什么 mutable default argument 是经典陷阱？](questions/01-python-semantics/q09.md) - ★★ · 极高
- [Q10. global 和 nonlocal 有什么区别？LEGB 如何工作？](questions/01-python-semantics/q10.md) - ★★ · 高

### 02. 核心容器与哈希表

从 list/tuple/dict/set 的 API 进入复杂度、哈希契约、拷贝语义与工程选择。

- [Q11. list 和 tuple 的区别是什么？](questions/02-containers-hashing/q11.md) - ★ · 极高
- [Q12. list.append 为什么是摊还 O(1)？](questions/02-containers-hashing/q12.md) - ★★ · 高
- [Q13. 为什么 list.insert(0, x) / pop(0) 慢？](questions/02-containers-hashing/q13.md) - ★ · 高
- [Q14. Python dict 查找为什么平均 O(1)？](questions/02-containers-hashing/q14.md) - ★★★ · 极高
- [Q15. 什么对象可以作为 dict key？](questions/02-containers-hashing/q15.md) - ★★ · 极高
- [Q16. 为什么实现 __eq__ 后必须认真考虑 __hash__？](questions/02-containers-hashing/q16.md) - ★★★ · 高
- [Q17. dict 是否保证插入顺序？](questions/02-containers-hashing/q17.md) - ★ · 高
- [Q18. dict.get、setdefault、defaultdict 如何选择？](questions/02-containers-hashing/q18.md) - ★★ · 高
- [Q19. set 为什么能高效查重？](questions/02-containers-hashing/q19.md) - ★ · 极高
- [Q20. 浅拷贝和深拷贝有什么区别？](questions/02-containers-hashing/q20.md) - ★★ · 极高

### 03. 函数、闭包与装饰器

把函数当一等对象理解，掌握闭包、late binding、装饰器、缓存与调用签名。

- [Q21. *args 和 **kwargs 的本质是什么？](questions/03-functions-closures-decorators/q21.md) - ★ · 极高
- [Q22. positional-only 与 keyword-only 参数解决什么问题？](questions/03-functions-closures-decorators/q22.md) - ★★ · 中
- [Q23. 为什么说函数是一等对象？](questions/03-functions-closures-decorators/q23.md) - ★ · 高
- [Q24. 什么是闭包？](questions/03-functions-closures-decorators/q24.md) - ★★ · 极高
- [Q25. late binding closure 为什么会得到 [2,2,2]？](questions/03-functions-closures-decorators/q25.md) - ★★★ · 极高
- [Q26. 装饰器本质是什么？](questions/03-functions-closures-decorators/q26.md) - ★★ · 极高
- [Q27. 为什么 decorator 通常需要 functools.wraps？](questions/03-functions-closures-decorators/q27.md) - ★★ · 高
- [Q28. 如何实现带参数装饰器？](questions/03-functions-closures-decorators/q28.md) - ★★ · 高
- [Q29. lambda 与普通 def 的区别是什么？](questions/03-functions-closures-decorators/q29.md) - ★ · 中
- [Q30. functools.lru_cache 有哪些工程陷阱？](questions/03-functions-closures-decorators/q30.md) - ★★★ · 高

### 04. OOP 与 Python Data Model

理解属性访问、descriptor、MRO、super、metaclass 与 __slots__ 等高级机制。

- [Q31. __new__ 和 __init__ 有什么区别？](questions/04-oop-data-model/q31.md) - ★★★ · 高
- [Q32. 实例方法、classmethod、staticmethod 如何选择？](questions/04-oop-data-model/q32.md) - ★★ · 极高
- [Q33. Python 的“private”是怎么实现的？](questions/04-oop-data-model/q33.md) - ★★ · 高
- [Q34. __getattribute__ 和 __getattr__ 有什么区别？](questions/04-oop-data-model/q34.md) - ★★★★ · 高
- [Q35. 什么是 descriptor？为什么它如此重要？](questions/04-oop-data-model/q35.md) - ★★★★★ · 高
- [Q36. property 是如何工作的？](questions/04-oop-data-model/q36.md) - ★★★ · 高
- [Q37. MRO 是什么？C3 linearization 解决什么问题？](questions/04-oop-data-model/q37.md) - ★★★★ · 高
- [Q38. super() 为什么不是“调用父类”？](questions/04-oop-data-model/q38.md) - ★★★★ · 高
- [Q39. 什么是 metaclass？什么时候真的需要？](questions/04-oop-data-model/q39.md) - ★★★★★ · 中
- [Q40. __slots__ 有什么用？有哪些坑？](questions/04-oop-data-model/q40.md) - ★★★★ · 高

### 05. 迭代器、生成器与资源管理

掌握惰性计算、迭代协议、generator delegation 与 context manager。

- [Q41. iterable 和 iterator 有什么区别？](questions/05-iterators-generators-context/q41.md) - ★★ · 极高
- [Q42. iter(x) 实际发生了什么？](questions/05-iterators-generators-context/q42.md) - ★★★ · 高
- [Q43. generator 与普通函数有什么区别？](questions/05-iterators-generators-context/q43.md) - ★★ · 极高
- [Q44. 为什么 generator 通常更省内存？](questions/05-iterators-generators-context/q44.md) - ★★ · 极高
- [Q45. generator.send() 有什么语义？](questions/05-iterators-generators-context/q45.md) - ★★★★ · 中
- [Q46. yield from 不只是语法糖吗？](questions/05-iterators-generators-context/q46.md) - ★★★★ · 中
- [Q47. 为什么 generator/iterator 通常只能消费一次？](questions/05-iterators-generators-context/q47.md) - ★★ · 高
- [Q48. context manager 的核心协议是什么？](questions/05-iterators-generators-context/q48.md) - ★★ · 极高
- [Q49. with 为什么比手写 try/finally 更好？](questions/05-iterators-generators-context/q49.md) - ★★ · 高
- [Q50. contextlib.contextmanager 是如何把 generator 变成上下文管理器的？](questions/05-iterators-generators-context/q50.md) - ★★★ · 中

### 06. CPython、内存、GC 与 Import

区分语言规范与 CPython 实现，理解引用计数、循环 GC、分配器与导入系统。

- [Q51. CPython 如何管理对象生命周期？](questions/06-cpython-memory-import/q51.md) - ★★★★ · 极高
- [Q52. del x 是否等于删除对象？](questions/06-cpython-memory-import/q52.md) - ★★ · 极高
- [Q53. 什么是 reference cycle？循环 GC 为什么需要它？](questions/06-cpython-memory-import/q53.md) - ★★★ · 高
- [Q54. weakref 适合解决什么问题？](questions/06-cpython-memory-import/q54.md) - ★★★ · 中
- [Q55. 为什么对象释放后进程 RSS 不一定下降？](questions/06-cpython-memory-import/q55.md) - ★★★★ · 中
- [Q56. sys.getsizeof 为什么不是对象“总内存”？](questions/06-cpython-memory-import/q56.md) - ★★ · 高
- [Q57. Python import 的核心流程是什么？](questions/06-cpython-memory-import/q57.md) - ★★★ · 高
- [Q58. circular import 为什么会产生 partially initialized module？](questions/06-cpython-memory-import/q58.md) - ★★★ · 极高
- [Q59. .pyc 是什么？什么时候会失效？](questions/06-cpython-memory-import/q59.md) - ★★ · 中
- [Q60. monkey patching 什么时候有用，为什么危险？](questions/06-cpython-memory-import/q60.md) - ★★★ · 中

### 07. 线程、进程、GIL 与多核并行

掌握经典 GIL 模型，并覆盖 Python 3.14 的 free-threaded 与 InterpreterPoolExecutor。

- [Q61. GIL 是什么？如何用现代版本回答？](questions/07-threads-processes-gil/q61.md) - ★★★ · 极高
- [Q62. “有 GIL 所以不需要锁”为什么是错的？](questions/07-threads-processes-gil/q62.md) - ★★★ · 极高
- [Q63. Python 3.14 free-threaded CPython 改变了什么？](questions/07-threads-processes-gil/q63.md) - ★★★★★ · 高
- [Q64. Thread vs Process 应该怎么选？](questions/07-threads-processes-gil/q64.md) - ★★★ · 极高
- [Q65. 多进程的主要代价是什么？](questions/07-threads-processes-gil/q65.md) - ★★ · 高
- [Q66. multiprocessing 为什么经常出现 pickle error？](questions/07-threads-processes-gil/q66.md) - ★★★ · 高
- [Q67. ThreadPoolExecutor 与 ProcessPoolExecutor 的关键差异？](questions/07-threads-processes-gil/q67.md) - ★★ · 极高
- [Q68. fork、spawn、forkserver 有什么区别？](questions/07-threads-processes-gil/q68.md) - ★★★★ · 高
- [Q69. 什么是 race condition？如何系统治理？](questions/07-threads-processes-gil/q69.md) - ★★ · 极高
- [Q70. Python 3.14 InterpreterPoolExecutor 是什么？](questions/07-threads-processes-gil/q70.md) - ★★★★★ · 高

### 08. asyncio 与结构化并发

从 event loop 到 TaskGroup、取消传播、限流、背压与生产级 worker。

- [Q71. concurrency 与 parallelism 有什么区别？](questions/08-asyncio-concurrency/q71.md) - ★ · 极高
- [Q72. coroutine、Task、Future 分别是什么？](questions/08-asyncio-concurrency/q72.md) - ★★★ · 极高
- [Q73. await 的核心语义是什么？](questions/08-asyncio-concurrency/q73.md) - ★★ · 极高
- [Q74. 为什么 async 函数里 time.sleep 是严重问题？](questions/08-asyncio-concurrency/q74.md) - ★ · 极高
- [Q75. asyncio.gather 与 TaskGroup 怎么选？](questions/08-asyncio-concurrency/q75.md) - ★★★★ · 极高
- [Q76. 为什么不能随便吞 asyncio.CancelledError？](questions/08-asyncio-concurrency/q76.md) - ★★★★ · 极高
- [Q77. async code 中如何调用阻塞函数？](questions/08-asyncio-concurrency/q77.md) - ★★ · 极高
- [Q78. async 能解决 CPU-bound 吗？](questions/08-asyncio-concurrency/q78.md) - ★★ · 极高
- [Q79. Semaphore 在 async 服务中解决什么问题？](questions/08-asyncio-concurrency/q79.md) - ★★ · 高
- [Q80. 如何设计一个生产级 asyncio worker？](questions/08-asyncio-concurrency/q80.md) - ★★★★★ · 极高

### 09. Typing、测试、打包与工程质量

掌握现代类型系统、dataclass、测试边界、依赖隔离与 pyproject.toml。

- [Q81. 动态语言为什么仍需要 type hints？](questions/09-typing-testing-packaging/q81.md) - ★ · 极高
- [Q82. Any 和 object 有什么区别？](questions/09-typing-testing-packaging/q82.md) - ★★★ · 高
- [Q83. Protocol 解决了什么问题？](questions/09-typing-testing-packaging/q83.md) - ★★★★ · 高
- [Q84. TypeVar / 新泛型语法解决什么问题？](questions/09-typing-testing-packaging/q84.md) - ★★★★ · 高
- [Q85. ParamSpec 为什么适合给装饰器做 typing？](questions/09-typing-testing-packaging/q85.md) - ★★★★★ · 中
- [Q86. dataclass 解决了什么？有哪些陷阱？](questions/09-typing-testing-packaging/q86.md) - ★★ · 极高
- [Q87. unit test 与 integration test 如何划分？](questions/09-typing-testing-packaging/q87.md) - ★★ · 高
- [Q88. mock 应该 mock 什么？](questions/09-typing-testing-packaging/q88.md) - ★★★ · 极高
- [Q89. virtual environment / lockfile 分别解决什么问题？](questions/09-typing-testing-packaging/q89.md) - ★★ · 高
- [Q90. pyproject.toml 在现代 Python 项目中的角色？](questions/09-typing-testing-packaging/q90.md) - ★★★ · 高

### 10. 性能优化、Web 后端与系统设计

把语言知识落到 profiling、内存、流处理、缓存和高并发 API 的综合场景。

- [Q91. Python 程序慢，第一步该做什么？](questions/10-performance-backend-design/q91.md) - ★★ · 极高
- [Q92. list comprehension 为什么经常比显式 for 更快？](questions/10-performance-backend-design/q92.md) - ★★ · 中
- [Q93. 为什么 NumPy 往往比 Python for loop 快很多？](questions/10-performance-backend-design/q93.md) - ★★★ · 极高
- [Q94. 如何系统定位 Python memory leak？](questions/10-performance-backend-design/q94.md) - ★★★★ · 极高
- [Q95. Django / Flask / FastAPI 应如何选择？](questions/10-performance-backend-design/q95.md) - ★★★ · 高
- [Q96. FastAPI async def endpoint 为什么仍可能很慢？](questions/10-performance-backend-design/q96.md) - ★★★ · 极高
- [Q97. 手写 LRU Cache，为什么常用 HashMap + Doubly Linked List？](questions/10-performance-backend-design/q97.md) - ★★★★ · 极高
- [Q98. 100GB 日志不能进内存，如何处理？](questions/10-performance-backend-design/q98.md) - ★★★ · 极高
- [Q99. 1 亿 URL 找 Top-K，如何设计？](questions/10-performance-backend-design/q99.md) - ★★★★ · 高
- [Q100. 设计高并发 Python API，如何选择整体并发模型？](questions/10-performance-backend-design/q100.md) - ★★★★★ · 极高

## 文档站点

本仓库自带 `mkdocs.yml`。安装并启动：

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 自动校验

```bash
python scripts/validate_repo.py
```

预期：`OK: 100 question markdown files validated.`

## 仓库原则

- 版本敏感事实优先引用 Python 官方文档 / PEP。
- 对 CPython 实现细节明确标注实现边界。
- 不把公开高频题型包装成无法验证的“某大厂内部原题”。
- 借鉴题目驱动型技术书的学习方法，但不复制任何受版权保护书籍的具体文字、题解或版式。

## 发布前建议

仓库没有替你选择内容许可证。正式公开发布前，请根据你的发布目标选择合适的 LICENSE，并确认 PDF 与文字内容的授权方式。
