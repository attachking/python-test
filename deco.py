class Test(object):

    def __init__(self, func):
        print('__init__')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('__call__')
        return self.func(*args, **kwargs)


@Test
def test2():
    pass


test2()
test2()
