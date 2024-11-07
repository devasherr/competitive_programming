# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = []
        q = deque([root])

        while q:
            total = 0            
            for _ in range(len(q)):
                cur = q.popleft()
                total += cur.val

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levelSum.append(total)
        
        root.val = 0
        level = 1
        q = deque([root])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                leftVal = cur.left.val if cur.left else 0
                rightVal = cur.right.val if cur.right else 0

                if cur.left:
                    cur.left.val = levelSum[level] - (leftVal + rightVal)
                    q.append(cur.left)
                if cur.right:
                    cur.right.val = levelSum[level] - (leftVal + rightVal)
                    q.append(cur.right)
            level += 1
        
        return root