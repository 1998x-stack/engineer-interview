# 对应题目：Q66 multiprocessing 为什么经常出现 pickle error？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def worker(x):
    return x * x

if __name__ == '__main__':
    with ProcessPoolExecutor() as ex:
        print(list(ex.map(worker, range(10))))
