from __future__ import annotations
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total=sum(nums)
        if total%k: return False
        target=total//k; nums.sort(reverse=True)
        if nums[0]>target: return False
        buckets=[0]*k
        def dfs(i):
            if i==len(nums): return True
            x=nums[i]; seen=set()
            for b in range(k):
                if buckets[b] in seen or buckets[b]+x>target: continue
                seen.add(buckets[b]); buckets[b]+=x
                if dfs(i+1): return True
                buckets[b]-=x
                if buckets[b]==0: break
            return False
        return dfs(0)
