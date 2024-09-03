# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, cur, remaining):
            if not root:
                return
            
            cur.append(root.val)
            if not root.left and not root.right and remaining == root.val:
                res.append(cur[:])
            
            dfs(root.left, cur, remaining - root.val)
            dfs(root.right, cur, remaining - root.val)
            cur.pop()
        dfs(root, [], targetSum)
        return res