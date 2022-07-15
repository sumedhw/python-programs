
def sumOfdigit(n):
    assert n>=0 and int(n) == n, "The number has to be a positive integer only"
    if n == 0:
        return 0
    else:
        return (n%10) + ( sumOfdigit(n//10) )


print(sumOfdigit(2334))