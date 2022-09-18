def f(t='default'):
    print(t)


def concatenation(*params):
    res: str = ''
    for item in params:
        res += item
    return res