import builtins as b


def print1(a, a1):
    b.print(a + a1)
    print('****' * 2)
    pass
    pass
    return 'print1'


b.print(print1('a', 'b'))
