# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        def dfs(root, p, q):
            if p.val <= root.val and q.val >= root.val:
                return root
            if p.val >= root.val and q.val <= root.val:
                return root
            
            if (p.val < root.val and q.val < root.val):
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        return dfs(root, p, q)
