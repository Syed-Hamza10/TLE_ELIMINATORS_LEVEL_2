#T: C : SQRT(N)
def foo(n):
    ans = []
    d = 2

    while d * d < n:

        if n % d == 0:
            ans.append(d)

            while n % d  == 0:
                n //= d
        d += 1

    if n > 1:
        ans.append(n)
    print(ans)

foo(1000)


