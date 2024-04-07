#Task 01: Write a recursive function to convert decimal number to binary number. Return binary number
#in string form.


def binary(n, s = ''):
    
    if n == 0: return s[::-1]

    s += str(n%2)

    return binary(n // 2, s)


print(binary(10))
   