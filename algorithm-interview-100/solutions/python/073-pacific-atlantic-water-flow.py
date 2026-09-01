from __future__ import annotations
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m,n=len(heights),len(heights[0])
        def reach(starts):
            seen=set(starts); stack=list(starts)
            while stack:
                r,c=stack.pop()
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in seen and heights[nr][nc]>=heights[r][c]:
                        seen.add((nr,nc)); stack.append((nr,nc))
            return seen
        pac=[(0,c) for c in range(n)]+[(r,0) for r in range(m)]
        atl=[(m-1,c) for c in range(n)]+[(r,n-1) for r in range(m)]
        return [list(x) for x in reach(pac)&reach(atl)]
