# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        visit = set()
        q = deque([root])

        while q:
            node = q.popleft()
            visit.add(node.val)
            if len(visit) > 1: return False

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return len(visit) < 2