from __future__ import annotations
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent=list(range(len(edges)+1)); rank=[0]*len(parent)
        def find(x):
            while x!=parent[x]: parent[x]=parent[parent[x]]; x=parent[x]
            return x
        for a,b in edges:
            ra,rb=find(a),find(b)
            if ra==rb: return [a,b]
            if rank[ra]<rank[rb]: ra,rb=rb,ra
            parent[rb]=ra
            if rank[ra]==rank[rb]: rank[ra]+=1
        return []
