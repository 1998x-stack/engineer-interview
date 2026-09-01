from __future__ import annotations
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            if not (0<=r<m and 0<=c<n) or grid[r][c]==0: return 0
            grid[r][c]=0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        return max((dfs(r,c) for r in range(m) for c in range(n)), default=0)
