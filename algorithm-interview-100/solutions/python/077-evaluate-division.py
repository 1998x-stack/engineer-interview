from __future__ import annotations
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        g=defaultdict(list)
        for (a,b),v in zip(equations,values): g[a].append((b,v)); g[b].append((a,1/v))
        def solve(s,t):
            if s not in g or t not in g: return -1.0
            stack=[(s,1.0)]; seen={s}
            while stack:
                u,val=stack.pop()
                if u==t: return val
                for v,w in g[u]:
                    if v not in seen: seen.add(v); stack.append((v,val*w))
            return -1.0
        return [solve(a,b) for a,b in queries]
