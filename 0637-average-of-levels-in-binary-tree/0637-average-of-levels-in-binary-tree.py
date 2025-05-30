# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return 0
        res = []
        q = deque([root])

        while q:
            val = 0
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                val += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(val/qLen)
        return res
       