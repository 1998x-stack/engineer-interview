from __future__ import annotations
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0]); q=deque(); fresh=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2: q.append((r,c))
                elif grid[r][c]==1: fresh+=1
        minutes=0
        while q and fresh:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2; fresh-=1; q.append((nr,nc))
            minutes+=1
        return minutes if fresh==0 else -1
