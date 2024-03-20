from src.bar import CONSTANT_A, Smt, asdf_func, some_func


def another_func(flag: bool = True):
    a = some_func() * CONSTANT_A
    if not flag:
        b = asdf_func()
        return a * b
    return a

def foo_func(smt: Smt):
    a = smt.some_method()
    return a


def foo_func_with_class_instance():
    smt = Smt()
    return smt.some_method()