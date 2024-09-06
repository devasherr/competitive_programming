# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isPal(nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                if nums[l].val != nums[r].val:
                    return False
                l += 1
                r -= 1
            return True

        q = deque()
        if root: q.append(root)
        while q:
            if not isPal(q): return False
            for _ in range(len(q)):
                node = q.popleft()
                if node.val == 101: continue
                
                leftNode = node.left if node.left else TreeNode(101)
                rightNode = node.right if node.right else TreeNode(101)

                q.append(leftNode)
                q.append(rightNode)

        return True