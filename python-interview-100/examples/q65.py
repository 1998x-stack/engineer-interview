# 对应题目：Q65 多进程的主要代价是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# 把小任务批成 chunk 往往比逐条 submit 更高效
for chunk in chunks(data, 1000):
    pool.submit(process_chunk, chunk)
