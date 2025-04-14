# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, depth):
            if not root:
                return None, depth
            
            leftVal, leftDepth = dfs(root.left, depth+1)
            rightVal, rightDepth = dfs(root.right, depth+1)

            if leftDepth > rightDepth:
                return leftVal, leftDepth  
            elif rightDepth > leftDepth:
                return rightVal, rightDepth
            else:
                return root, rightDepth
        
        return dfs(root, 0)[0]