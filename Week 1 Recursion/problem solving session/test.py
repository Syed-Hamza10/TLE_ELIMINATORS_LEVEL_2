a = [1,2,3,4,5]

min = max = -1
 
for ele in a:
    if ele > max:
        max = ele
    elif ele < min:
        min = ele
print(min, max)