def binary_generator(s, n):
    if len(s) == n:
        print(s)
        return
    
    binary_generator(s + '0', n)
    binary_generator(s + '1', n)

binary_generator('', 3)