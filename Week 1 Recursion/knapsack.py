# problem link : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/U

def knapsack(i,n, W, arr):
        
    if i >= n:    
        if W >= 0: #knapsack fully exhausted
            return 0
        else:
            return -100000 # a very large number so it doesnt effect the results. It means knapsack is not fully exhausted

    notTake = knapsack(i + 1, n ,W, arr)
    Take = knapsack(i+1, n , W - arr[i][0], arr) + arr[i][1]

    return max( notTake, Take) 

if __name__ == '__main__':
    n, W = map(int,input().split())
    
    arr = []
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x,y))
    print(knapsack(0, n , W, arr))
    







