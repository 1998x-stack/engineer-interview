from __future__ import annotations
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        a, b = nums1, nums2; m, n = len(a), len(b)
        half = (m+n+1)//2; l, r = 0, m
        while l <= r:
            i = (l+r)//2; j = half-i
            al = float('-inf') if i==0 else a[i-1]; ar = float('inf') if i==m else a[i]
            bl = float('-inf') if j==0 else b[j-1]; br = float('inf') if j==n else b[j]
            if al <= br and bl <= ar:
                if (m+n)%2: return float(max(al, bl))
                return (max(al, bl)+min(ar, br))/2
            if al > br: r = i-1
            else: l = i+1
        raise ValueError('invalid input')
