# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        if node1.val != node2.val: return False

        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True

        def dfs(node):
            if not node: return False
            if self.isSameTree(node, subRoot): return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
