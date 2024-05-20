import math as m
def foo(n):
    a = []
    i = 1
    while i <= m.sqrt(n):
        if n % i == 0:
            a.append(i)
            if n // i != i:
                a.append(n // i)
        i += 1
    print(a)

foo(16)