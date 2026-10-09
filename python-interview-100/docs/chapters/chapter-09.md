# Chapter 09 - Typing、测试、打包与工程质量

掌握现代类型系统、dataclass、测试边界、依赖隔离与 pyproject.toml。

## 仓库增强版：章节深挖

### 深入学习路线

本章的共同主题是“把隐式约定变成机器可验证契约”：typing 约束接口，tests 约束行为，packaging/lock 约束构建环境。

**版本基线**：优先理解 PEP 695 新泛型语法，同时能识别旧 `TypeVar/ParamSpec` 写法。

**组合追问**：Q82→Q83→Q84→Q85；Q87→Q88；Q89→Q90。

## 本章目标

类型、测试、打包的共同目标是把隐式约束变成可自动检查的契约，并降低大型代码库中的变更成本。

## 题目列表

- [Q81. 动态语言为什么仍需要 type hints？](../questions/09-typing-testing-packaging/q81.md) - ★ / 极高
- [Q82. Any 和 object 有什么区别？](../questions/09-typing-testing-packaging/q82.md) - ★★★ / 高
- [Q83. Protocol 解决了什么问题？](../questions/09-typing-testing-packaging/q83.md) - ★★★★ / 高
- [Q84. TypeVar / 新泛型语法解决什么问题？](../questions/09-typing-testing-packaging/q84.md) - ★★★★ / 高
- [Q85. ParamSpec 为什么适合给装饰器做 typing？](../questions/09-typing-testing-packaging/q85.md) - ★★★★★ / 中
- [Q86. dataclass 解决了什么？有哪些陷阱？](../questions/09-typing-testing-packaging/q86.md) - ★★ / 极高
- [Q87. unit test 与 integration test 如何划分？](../questions/09-typing-testing-packaging/q87.md) - ★★ / 高
- [Q88. mock 应该 mock 什么？](../questions/09-typing-testing-packaging/q88.md) - ★★★ / 极高
- [Q89. virtual environment / lockfile 分别解决什么问题？](../questions/09-typing-testing-packaging/q89.md) - ★★ / 高
- [Q90. pyproject.toml 在现代 Python 项目中的角色？](../questions/09-typing-testing-packaging/q90.md) - ★★★ / 高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
