#problem link = https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/V



# def helper(arr, i, ans):
#     if i == n:
#         return ans == x
#     return helper(arr, i + 1, ans + arr[i]) or helper(arr, i + 1, ans - arr[i])

# if __name__ == "__main__":
#     n, x = map(int, input().split())
#     arr = list(map(int, input().split()))
#     if helper(arr, 1, arr[0]):
#         print("YES")
#     else:
#         print("NO")

found = False
def solve(X, elements,sum,i = 1):
    global found
    if sum == X and i == len(elements):
        found = True
        return
    if i >= len(elements) and sum != X:
        return
    solve(X, elements,sum + elements[i] , i+ 1 )
    #sum -= elements[i]
    solve(X, elements, sum - elements[i], i + 1 )

if __name__ == '__main__':
    N, X = map(int, input().split())
    elements = list(map(int, input().split()))
    sum = elements[0]
    solve(X, elements, sum)
    if found:
        print("YES")
    else:
        print("NO")



### SIMPLE APPROACH

def solve1(X, elements, sum, i = 0):
    if i >= len(elements):
        return sum == X
    return solve1(X, elements, sum + elements[i], i+1) or solve1(X, elements, sum - elements[i], i+1)
print(solve1(5, [1,2,3,4,5], 0 ))