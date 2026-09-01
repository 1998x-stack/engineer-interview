from __future__ import annotations
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0]+p[1]*p[1])
