def f(n, count = 1):
    if n <= 1: # base case
        return count
    if n % 2 == 0:
        return f(n // 2, count + 1)
    else:
        return f((3*n) + 1, count + 1)

n = int(input())
print(f(n))