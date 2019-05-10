a = 2


def func():
    b = a
    print(b)


def func2():
    global a
    print(a)


func()
func2()

dic = dict()
dic['a'] = 1
print(dic)


def func3(x, *k):
    print(x)
    print(k)


func3(1, 2, 3)

print(isinstance(func3, object))


def func4(x):
    def func5():
        # nonlocal x
        # x += 1
        return x * x

    return func5


print(func4(1) is func4(1))

print('duplicate values found in %r: %s' % (object, [('1', '2')]))
