# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # global
        self.res = 0
        def dfs(node):
            if not node:
                return [0, 0] # size, coins

            leftSize, leftCoin = dfs(node.left)
            rightSize, rightCoin = dfs(node.right)

            # with current coin
            curSize = leftSize + rightSize + 1
            curCoin = node.val + leftCoin + rightCoin

            self.res += abs(curCoin - curSize)
            return [curSize, curCoin]

        dfs(root)

        return self.res