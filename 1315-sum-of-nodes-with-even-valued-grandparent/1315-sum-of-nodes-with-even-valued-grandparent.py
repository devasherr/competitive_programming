# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        def dfs(root, parent, grand):
            if not root:
                return

            cur = root.val
            if grand and grand % 2 == 0:
                self.res += cur
            
            grand = parent
            parent = cur

            dfs(root.left, parent, grand)
            dfs(root.right, parent, grand)

        dfs(root, None, None)
        return self.res