
# time complexity o(n)
def sum_of_series(n):
    sum = 0
    for i in range(1,n+1):
        sum += pow(i,3)
    return sum

print(sum_of_series(7))


# using math formula
# time complexity -> o(1)

def sum_of_series_math(n):
    x = ( n * (n+1) / 2 )
    res = x * x

    return res

print(sum_of_series_math(5))


def sum_of_series_math_better(n):

    if n%2 == 0:
        x  = (n/2) * (n + 1)
    else:
        x = ( (n + 1) / 2 ) * n 

    x = ( n * (n+1) / 2 )
    res = x * x

    return res

print(sum_of_series_math_better(7))

