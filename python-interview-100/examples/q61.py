# 对应题目：Q61 GIL 是什么？如何用现代版本回答？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import threading
# 对 CPU-bound Python 循环，默认 CPython 多线程通常不会带来线性多核加速
# 对网络/文件等待，threads 仍可能显著提高并发度
