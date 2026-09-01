from __future__ import annotations
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        tmp = [0]*len(nums)
        def merge_sort(l, r):
            if r-l <= 1: return
            m=(l+r)//2; merge_sort(l,m); merge_sort(m,r)
            i,j,k=l,m,l
            while i<m or j<r:
                if j>=r or (i<m and nums[i] <= nums[j]): tmp[k]=nums[i]; i+=1
                else: tmp[k]=nums[j]; j+=1
                k+=1
            nums[l:r]=tmp[l:r]
        merge_sort(0,len(nums)); return nums
