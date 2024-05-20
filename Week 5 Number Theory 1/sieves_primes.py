def sieve_while(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    i = 2
    while i * i <= n:
        if primes[i]:
            j = i * i
            while j < n:
                primes[j] = False
                j += i
        i += 1    
    return primes

print(sieve_while(121))


def sieve_for(n):
    primes = [True] * n
    if n > 0: primes[0] = False
    if n > 1: primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return primes

print(sieve_for(121))
