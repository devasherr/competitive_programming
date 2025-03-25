# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(node, curSum, path):
            if not node: return
            curSum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if curSum == targetSum:
                    self.res.append(path[:])
                path.pop()
                return

            traverse(node.left, curSum, path)
            traverse(node.right, curSum, path)
            path.pop()
        
        traverse(root, 0, [])
        return self.res