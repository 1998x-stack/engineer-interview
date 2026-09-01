from __future__ import annotations
class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode | None') -> int:
        ans=0
        def depth(node):
            nonlocal ans
            if not node: return 0
            l,r=depth(node.left),depth(node.right)
            ans=max(ans,l+r)
            return 1+max(l,r)
        depth(root); return ans
