class Solution:
    def subsetsWithDup(self, nums):
        res = []
        subsets = []
        nums.sort()
        def dfs(idx):
            if idx >= len(nums):
                
                if subsets not in res:
                    res.append(subsets.copy())
                return
            #pick
            subsets.append(nums[idx])
            dfs( idx + 1)
            #not pick
            subsets.pop()
            dfs(idx + 1)
        dfs(0)
        return res