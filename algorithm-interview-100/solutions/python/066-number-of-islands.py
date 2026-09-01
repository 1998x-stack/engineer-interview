from __future__ import annotations
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n=len(grid),len(grid[0]); ans=0
        def dfs(r,c):
            if not (0<=r<m and 0<=c<n) or grid[r][c]!='1': return
            grid[r][c]='0'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1': ans+=1; dfs(r,c)
        return ans
