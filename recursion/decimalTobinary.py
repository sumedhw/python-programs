
from unicodedata import decimal


def decimalToBinay(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinay(int(n/2))

print(decimalToBinay(120))
