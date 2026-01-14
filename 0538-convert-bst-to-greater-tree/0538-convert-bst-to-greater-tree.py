# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None 
        nums = []
        def inorder(node):
            if not node: return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)

        numsMap = {nums[-1]: nums[-1]}
        for i in range(len(nums)-2, -1, -1):
            numsMap[nums[i]] = nums[i] + nums[i+1]
            nums[i] += nums[i+1]

        def construct(node):
            if not node: return None

            root = TreeNode(numsMap[node.val])
            root.left = construct(node.left)
            root.right = construct(node.right)

            return root

        return construct(root)
