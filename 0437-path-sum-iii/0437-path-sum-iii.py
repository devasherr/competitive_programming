# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def postorder(root):
            if not root:
                return [0, 0, 0]
            
            leftvals = postorder(root.left)
            rightvals = postorder(root.right)
            for i in range(3):
                leftvals[i] += root.val
            for i in range(3):
                rightvals[i] += root.val

            if targetSum in leftvals: self.res += 1
            if targetSum in rightvals: self.res += 1
            
            return [leftvals[1], root.val, rightvals[1]]

        postorder(root)
        return self.res