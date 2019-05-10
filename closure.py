def func():
    a = 20

    def func2():
        return a

    return func2


f = func()
# __closure__ 闭包的标志
print(f.__closure__)


def func3():
    a = 0

    def func4():
        nonlocal a
        a += 1
        return a

    return func4


f2 = func3()
print(f2())
print(f2())
print(f2())

