def func(n):
    if n == 1:
        return True
    
    if n == 0:
        return False
    
    if n % 4 != 0:
        return False
    
    return func(n / 4)

print(func(0))