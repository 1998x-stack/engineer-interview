from __future__ import annotations
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> 'TreeNode | None':
        pos={x:i for i,x in enumerate(inorder)}; pre_i=0
        def build(l,r):
            nonlocal pre_i
            if l>=r: return None
            val=preorder[pre_i]; pre_i+=1; m=pos[val]
            node=TreeNode(val); node.left=build(l,m); node.right=build(m+1,r)
            return node
        return build(0,len(inorder))
