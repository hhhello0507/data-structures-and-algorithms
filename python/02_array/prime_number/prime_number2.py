n = 31

def is_prime_number(n):
    if n % 2 == 0:
        return True
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True

result = is_prime_number(n)
print(result)