from __future__ import annotations
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]; path=[]
        def dfs(i):
            if i==len(nums): ans.append(path.copy()); return
            dfs(i+1)
            path.append(nums[i]); dfs(i+1); path.pop()
        dfs(0); return ans
