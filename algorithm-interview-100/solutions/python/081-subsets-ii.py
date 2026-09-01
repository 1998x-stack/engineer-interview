from __future__ import annotations
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort(); ans=[]; path=[]
        def dfs(start):
            ans.append(path.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]: continue
                path.append(nums[i]); dfs(i+1); path.pop()
        dfs(0); return ans
