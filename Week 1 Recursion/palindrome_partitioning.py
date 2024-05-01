#problem link : https://leetcode.com/problems/palindrome-partitioning/description/

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def partition(s):
    res = []
    #subset = []

    def dfs(idx, subset):
        
        if idx >= len(s):
            #print(subset)
            if subset not in res:
                res.append(subset.copy())
            return            
        
        for i in range(idx, len(s)):
            if is_palindrome(s[idx : i+1]):
                subset.append(s[idx : i+1])
                dfs(i + 1, subset)
                subset.pop()
                   
    dfs(0, [])
    print(res)

partition('aab')

