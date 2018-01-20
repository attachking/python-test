def log(fn):
    def dec(*args, **kwargs):
        print(fn.__name__)
        return fn(*args, **kwargs)
    return dec


@log
def _fn():
    print('2018')


_fn()
