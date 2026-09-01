from __future__ import annotations
class Solution:
    def isValidBST(self, root: 'TreeNode | None') -> bool:
        def dfs(node, lo, hi):
            if not node: return True
            if not (lo < node.val < hi): return False
            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
        return dfs(root, float('-inf'), float('inf'))
