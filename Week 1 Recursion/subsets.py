# def binary_generator(s, n):
#     if len(s) == n:
#         print(s)
#         return
#     binary_generator(s + '0', n)
#     binary_generator(s + '1', n)
# binary_generator('', 3)
def subsets(numbers):
    res = []
    subset = []

    def dfs(idx):
        if idx >= len(numbers):
            print(subset)
            if subset not in res:
                res.append(subset.copy())
            return
        #pick
        subset.append(numbers[idx])
        dfs( idx + 1)
        #not pick
        subset.pop()
        dfs(idx + 1)
    dfs(0)
    return res

print(subsets([1,2,2]))
