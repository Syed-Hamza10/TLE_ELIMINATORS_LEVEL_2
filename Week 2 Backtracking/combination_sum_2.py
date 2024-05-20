# link : https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates, target: int): 
        self.res = []
        def dfs(i, cur, total):
            if total == target:
                self.res.append(cur.copy())
                return
        
            if i >= len(candidates) or total > target:
                return
    
            
            
   
            #pick
            cur.append(candidates[i])

            dfs(i+1, cur, total+candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            #not pick

            dfs(i+1, cur, total)
        candidates.sort()    
        dfs(0, [], 0)   
        return self.res