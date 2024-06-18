# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, cur):
            if not root:
                return
            if not root.left and not root.right:
                cur += str(root.val)
                self.res += int(cur)
                cur = cur[:-1]
                return
            
            cur += str(root.val)
            dfs(root.left, cur)
            dfs(root.right, cur)

        dfs(root, "")

        return self.res