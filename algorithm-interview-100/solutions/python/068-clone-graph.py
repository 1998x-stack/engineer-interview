from __future__ import annotations
class Solution:
    def cloneGraph(self, node: 'Node | None') -> 'Node | None':
        if not node: return None
        copies={}
        def dfs(cur):
            if cur in copies: return copies[cur]
            copy=Node(cur.val); copies[cur]=copy
            copy.neighbors=[dfs(n) for n in cur.neighbors]
            return copy
        return dfs(node)
