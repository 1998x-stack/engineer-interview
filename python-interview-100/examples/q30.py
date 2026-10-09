# 对应题目：Q30 functools.lru_cache 有哪些工程陷阱？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from functools import lru_cache

@lru_cache(maxsize=1024)
def parse_schema(text: str):
    return expensive_parse(text)

# parse_schema.cache_info()
# parse_schema.cache_clear()
