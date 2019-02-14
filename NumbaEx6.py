from numba import jit

@jit
def add1(x):
    return x + 1

@jit
def bar(fn, x):
    return fn(x)

@jit
def foo(x):
    return bar(add1, x)

# Passing add1 within numba compiled code.
print(foo(1))
# Passing add1 into bar from interpreted code
print(bar(add1, 1))
