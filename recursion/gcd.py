 
def gcd(a,b):
    assert int(a) == a and int(b) == b, "The numbers must be integer only !"
    if a < 0:
        return -1 * a

    if b < 0 :
        return -1 * b

    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(48,18))