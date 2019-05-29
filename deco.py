class Test(object):

    def __init__(self, func):
        print('__init__')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('__call__')
        return self.func(*args, **kwargs)


def dec(func):
    def wrapper():
        print('222')
        return func()

    return wrapper


@Test
@dec
def test2():
    pass


test2()
# test2()
