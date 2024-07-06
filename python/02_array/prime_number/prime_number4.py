n = 31

def get_primes_until(n):
    prime_number_list = [2]
    for i in range(3, n + 1, 2):
        t = True
        for prime_number in prime_number_list:
            if prime_number ** 0.5 > i:
                break
            if i % prime_number == 0:
                t = False
                break
        if t:
            prime_number_list.append(i)
    return prime_number_list

result = get_primes_until(n)
print(result)