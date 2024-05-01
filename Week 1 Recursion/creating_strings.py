#problem link : https://cses.fi/problemset/task/1622


#a= [ ]
p = set()
def create_string(s, i):
    p.add(s)
    if i <= 0:
        return
    for _ in range(len(s)):
        # if s not in a:
        #     a.append(s)
        # else:
        x = list(s) # converts to list
        x[-i], x[ -i + 1 ] = x[-i + 1], x[-i] #swapping
        s = ''.join(x) # back to string
        #print(s)
        create_string(s, i - 1 ) #recursive call


if __name__ == '__main__':
    s = input()
    s = ''.join(sorted(s)) #sorts s
    #print(s)
    i = len(s) - 1
    #a.append(s)
    create_string(s, i)
    print(p)
    
    #print(a)