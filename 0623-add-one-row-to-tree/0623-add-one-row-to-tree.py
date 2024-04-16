# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = deque([root])

        while depth - 1 > 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth -= 1

        while q:
            node = q.popleft()
            leftNode = TreeNode(val, node.left, None)
            rightNode = TreeNode(val, None, node.right)

            node.left = leftNode
            node.right = rightNode
            
        return root