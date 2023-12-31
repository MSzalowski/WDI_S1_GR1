def is_prime(n):
    if n < 2:
        return False    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(-2))

def prime_numbers(n, m):
    primes = []
    for i in range(n, m+1):
        if is_prime(i):
            primes.append(i)
    return primes

print(prime_numbers(8, 24))