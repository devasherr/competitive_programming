# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, path, val):
            if not node: return True
            if path == "l" and node.val >= val: return False
            if path == "r" and node.val <= val: return False

            return dfs(node.left, "l", min(node.val, val)) and dfs(node.right, "r", max(node.val, val))

        return dfs(root, "", root.val)
