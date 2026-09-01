from __future__ import annotations
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans=[]; path=[]
        def dfs(start):
            if start==len(s): ans.append(path.copy()); return
            for end in range(start+1,len(s)+1):
                piece=s[start:end]
                if piece==piece[::-1]: path.append(piece); dfs(end); path.pop()
        dfs(0); return ans
