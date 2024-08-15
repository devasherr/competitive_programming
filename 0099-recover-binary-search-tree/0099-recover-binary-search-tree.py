# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nums = []
        def inorder(node):
            if not node: return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        badOnes = []
        for n1, n2 in zip(sorted(nums), nums):
            if n1 != n2:
                badOnes.append(n2)
        
        badMap = {badOnes[0]:badOnes[1], badOnes[1]:badOnes[0]}
        def dfs(node):
            if not node: return
            if node.val in badMap:
                node.val = badMap[node.val]

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)