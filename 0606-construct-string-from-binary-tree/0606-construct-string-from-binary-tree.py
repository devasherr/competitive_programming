# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def preorder(root):
            if not root: return
            self.res.append(str(root.val))
            if not root.left and root.right:
                self.res.append("(")
                self.res.append(")")
            
            if root.left:
                self.res.append("(")
                preorder(root.left)
                self.res.append(")")
            if root.right:
                self.res.append("(")
                preorder(root.right)
                self.res.append(")")
                
        preorder(root)
        return "".join(self.res)