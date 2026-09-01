from __future__ import annotations
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]; cols=set(); diag1=set(); diag2=set(); board=[['.']*n for _ in range(n)]
        def dfs(r):
            if r==n: ans.append([''.join(row) for row in board]); return
            for c in range(n):
                if c in cols or r-c in diag1 or r+c in diag2: continue
                cols.add(c); diag1.add(r-c); diag2.add(r+c); board[r][c]='Q'
                dfs(r+1)
                board[r][c]='.'; cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)
        dfs(0); return ans
