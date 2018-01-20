# 函数def或类class声明后需空出两个空行
def fact(n, t=1):
    if not (isinstance(n, int) and isinstance(n, (int, float))):
        raise TypeError('参数必须为int或float类型')
    if n == 1:
        return t
    else:
        t = t * n
        return fact(n - 1, t)


print(fact(100))
print([1, 2, 3, 4, 5][-2:])
