# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, val):
            if not cur:
                return 0

            # for the extra zero we want
            val *= 10 
            val += cur.val
        
            if not cur.left and not cur.right:
                return val
            return dfs(cur.left, val) + dfs(cur.right, val)
        return dfs(root, 0)