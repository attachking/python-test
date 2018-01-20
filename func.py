# 列出所有质数
def _odd_():
    # 初始化序列(从3开始的奇数)
    _n = 1
    while True:
        _n = _n + 2
        yield _n


def _fil(_n):
    # 筛选函数
    return lambda x: x % _n > 0


def _pro():
    odd = _odd_()
    while True:
        # 取第一个数
        _n = next(odd)
        yield _n
        # 重新构造序列
        odd = filter(_fil(_n), odd)


gen = _pro()
n = next(gen)
while n < 10000000:
    print(n)
    n = next(gen)
