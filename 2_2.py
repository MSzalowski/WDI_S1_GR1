def fib_iterative(n):
    if n == 0 or n == 1:
        return 1
    fibs = [1, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

print(fib_iterative(20))

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Tests
print(fib(20))