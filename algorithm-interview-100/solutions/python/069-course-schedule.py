from __future__ import annotations
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g=[[] for _ in range(numCourses)]; indeg=[0]*numCourses
        for a,b in prerequisites: g[b].append(a); indeg[a]+=1
        q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
        while q:
            u=q.popleft(); seen+=1
            for v in g[u]:
                indeg[v]-=1
                if indeg[v]==0: q.append(v)
        return seen==numCourses
