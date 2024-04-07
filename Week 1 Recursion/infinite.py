#writes a recursive function that prints number of times it has run

def infinite(n):
    
    print(n)

    infinite(n+1)

print(infinite(0))

