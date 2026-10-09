# 对应题目：Q67 ThreadPoolExecutor 与 ProcessPoolExecutor 的关键差异？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

with ThreadPoolExecutor(max_workers=8) as ex:
    futures = [ex.submit(fetch, u) for u in urls]
    for f in futures:
        handle(f.result())
