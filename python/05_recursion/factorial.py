def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)

n = 20
result = factorial(20)

print(result)