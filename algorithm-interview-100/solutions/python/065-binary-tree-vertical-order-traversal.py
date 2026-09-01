from __future__ import annotations
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: 'TreeNode | None') -> list[list[int]]:
        if not root: return []
        cols=defaultdict(list); q=deque([(root,0)]); lo=hi=0
        while q:
            node,c=q.popleft(); cols[c].append(node.val); lo=min(lo,c); hi=max(hi,c)
            if node.left: q.append((node.left,c-1))
            if node.right: q.append((node.right,c+1))
        return [cols[c] for c in range(lo,hi+1)]
