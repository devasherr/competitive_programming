# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = root.val

        while q:
            for _ in range(len(q)):
                cur = []
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    cur.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    cur.append(node.right.val)

                if cur:
                    res = cur[0]

        return res