#problem link : https://codeforces.com/contest/26/problem/A


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def almostPrime(n):
    for i in range(2,n):
        if isPrime(i) and n % i == 0:
            return True
    return False
n = int(input())
count = 0
for i in range(1, n):
    if almostPrime(i):
        count += 1
print(count)