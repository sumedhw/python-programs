
def fact(n):
    assert n>=0 and int(n) == n, "Fibonacci number cannot be negative number or non integer"
    if n<1:
        return 1
    else:
        return n * fact(n-1)


print(fact(4))