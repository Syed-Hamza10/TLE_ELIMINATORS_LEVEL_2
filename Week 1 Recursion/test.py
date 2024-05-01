def isPrime():
    should_continue = True

    num = int(input())
    i = 1
    count = 0
    while should_continue:
        if num % i == 0 :
            return False
        elif num % i == 0 and count == 2:
            count +=1            
        i += 1
    return True


print(isPrime())