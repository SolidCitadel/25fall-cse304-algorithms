# name: 전현준
# student id: 2021105636
def fib1(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)