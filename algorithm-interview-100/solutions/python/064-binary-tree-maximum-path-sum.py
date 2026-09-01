from __future__ import annotations
class Solution:
    def maxPathSum(self, root: 'TreeNode') -> int:
        ans=float('-inf')
        def gain(node):
            nonlocal ans
            if not node: return 0
            l=max(0,gain(node.left)); r=max(0,gain(node.right))
            ans=max(ans,node.val+l+r)
            return node.val+max(l,r)
        gain(root); return int(ans)
