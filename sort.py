def sort_by_name(st):
    return st[0].lower()


li1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
li2 = sorted(li1, key=sort_by_name, reverse=True)
print(li2)


def create_counter():
    _num = 0

    def f():
        # 闭包引用的外部变量如果是不可变的，且需要在返回的函数中修改，则要在函数中用nonlocal声明
        nonlocal _num
        _num = _num + 1
        return _num

    return f


n1 = create_counter()
print(n1())
print(n1())
print(n1())
