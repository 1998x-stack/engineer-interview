from __future__ import annotations
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if type(k) is not int or k < 1 or k > len(nums):
            raise ValueError('k must be in [1, len(nums)]')
        if any(type(x) is not int or x <= 0 for x in nums):
            raise ValueError('the backtracking pruning requires positive integers')
        total=sum(nums)
        if total%k: return False
        target=total//k; ordered=sorted(nums, reverse=True)
        if ordered[0]>target: return False
        buckets=[0]*k
        def dfs(i):
            if i==len(nums): return True
            x=ordered[i]; seen=set()
            for b in range(k):
                if buckets[b] in seen or buckets[b]+x>target: continue
                seen.add(buckets[b]); buckets[b]+=x
                if dfs(i+1): return True
                buckets[b]-=x
                if buckets[b]==0: break
            return False
        return dfs(0)
