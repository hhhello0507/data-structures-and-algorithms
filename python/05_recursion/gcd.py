def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = 9
b = 36

result = gcd(a, b)
print(result)
