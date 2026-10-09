# 对应题目：Q100 设计高并发 Python API，如何选择整体并发模型？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# 一个常见分层
# Client -> API/ASGI workers -> async DB/HTTP
#                         -> bounded job queue -> CPU workers
#                         -> cache
# 全链路都有 timeout/backpressure/metrics
