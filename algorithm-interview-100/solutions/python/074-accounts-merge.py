from __future__ import annotations
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        parent={}; owner={}
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x: parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            ra,rb=find(a),find(b)
            if ra!=rb: parent[rb]=ra
        for acc in accounts:
            name,*emails=acc
            for e in emails: owner[e]=name; parent.setdefault(e,e)
            for e in emails[1:]: union(emails[0],e)
        groups=defaultdict(list)
        for e in parent: groups[find(e)].append(e)
        return [[owner[root]]+sorted(emails) for root,emails in groups.items()]
