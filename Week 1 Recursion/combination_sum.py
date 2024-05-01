# link : https://leetcode.com/problems/combination-sum/

res = []
candidates = [2,3,6,7]
target = 7
def dfs(i, cur, total):
        if i >= len(candidates) or total > target:
            return

        if total == target:
            res.append(cur.copy())
            return
        

        #pick
        cur.append(candidates[i])

        dfs(i, cur, total+candidates[i])

        cur.pop()

        #not pick

        dfs(i+1, cur, total)     

dfs(0,[],0)
print(res)