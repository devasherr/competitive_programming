# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node.left and val < node.val:
                node.left = TreeNode(val)
                return
            if not node.right and val > node.val:
                node.right = TreeNode(val)
                return
            
            if node.left and val < node.val:
                dfs(node.left)
            if node.right and val > node.val:
                dfs(node.right)
        
        dfs(root)
        return root