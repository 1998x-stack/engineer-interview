from __future__ import annotations
from collections import deque

class Solution:
    def rightSideView(self, root: 'TreeNode | None') -> list[int]:
        if not root: return []
        q=deque([root]); ans=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(node.val)
        return ans
