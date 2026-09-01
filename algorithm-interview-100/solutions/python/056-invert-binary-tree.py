from __future__ import annotations
class Solution:
    def invertTree(self, root: 'TreeNode | None') -> 'TreeNode | None':
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
