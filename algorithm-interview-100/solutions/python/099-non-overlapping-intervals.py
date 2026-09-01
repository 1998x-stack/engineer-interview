from __future__ import annotations
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1]); end=float('-inf'); kept=0
        for s,e in intervals:
            if s>=end: kept+=1; end=e
        return len(intervals)-kept
