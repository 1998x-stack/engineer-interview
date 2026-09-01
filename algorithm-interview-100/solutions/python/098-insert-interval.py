from __future__ import annotations
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans=[]; i=0; n=len(intervals); s,e=newInterval
        while i<n and intervals[i][1]<s: ans.append(intervals[i]); i+=1
        while i<n and intervals[i][0]<=e:
            s=min(s,intervals[i][0]); e=max(e,intervals[i][1]); i+=1
        ans.append([s,e]); ans.extend(intervals[i:]); return ans
