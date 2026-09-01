from __future__ import annotations
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g=[[] for _ in range(numCourses)]; indeg=[0]*numCourses
        for a,b in prerequisites: g[b].append(a); indeg[a]+=1
        q=deque(i for i,d in enumerate(indeg) if d==0); order=[]
        while q:
            u=q.popleft(); order.append(u)
            for v in g[u]:
                indeg[v]-=1
                if indeg[v]==0: q.append(v)
        return order if len(order)==numCourses else []
