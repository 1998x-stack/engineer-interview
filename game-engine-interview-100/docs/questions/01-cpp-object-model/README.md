# 第 1 章 · C++ 对象模型与语言机制

从“会写 C++”升级到理解 ABI、对象生命周期、资源所有权、容器语义与引擎级元编程。

## 本章能力目标

- ABI / object model
- ownership / RAII
- move semantics
- container invalidation
- reflection / codegen

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q001](Q001.md) | C++ 虚函数和运行时多态到底是怎么实现的？ | Advanced | `cpp, engine-core` |
| [Q002](Q002.md) | 为什么基类析构函数经常必须是 virtual？ | Intermediate | `cpp, engine-core, virtual-dispatch` |
| [Q003](Q003.md) | 为什么构造函数不能是 virtual？构造期间调用 virtual function 会怎样？ | Intermediate | `cpp, engine-core, virtual-dispatch` |
| [Q004](Q004.md) | unique_ptr、shared_ptr、weak_ptr 底层有什么区别？ | Advanced | `cpp, engine-core, smart-pointer` |
| [Q005](Q005.md) | shared_ptr 为什么会发生循环引用？如何从设计上避免？ | Intermediate | `cpp, engine-core, smart-pointer` |
| [Q006](Q006.md) | 左值、右值、std::move、移动构造究竟解决什么问题？ | Intermediate | `cpp, engine-core` |
| [Q007](Q007.md) | std::vector 扩容时发生了什么？哪些引用会失效？ | Intermediate | `cpp, engine-core, stl` |
| [Q008](Q008.md) | vector 为什么常常比 list 更快，即使 list 插入是 O(1)？ | Intermediate | `cpp, engine-core, stl` |
| [Q009](Q009.md) | new/delete 与 malloc/free 有什么区别？为什么不能混用？ | Intermediate | `cpp, engine-core` |
| [Q010](Q010.md) | C++ Reflection 为什么难？游戏引擎如何实现反射？ | Advanced | `cpp, engine-core, reflection` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
