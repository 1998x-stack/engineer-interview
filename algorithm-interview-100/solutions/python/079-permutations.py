from __future__ import annotations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]; path=[]; used=[False]*len(nums)
        def dfs():
            if len(path)==len(nums): ans.append(path.copy()); return
            for i,x in enumerate(nums):
                if used[i]: continue
                used[i]=True; path.append(x); dfs(); path.pop(); used[i]=False
        dfs(); return ans
