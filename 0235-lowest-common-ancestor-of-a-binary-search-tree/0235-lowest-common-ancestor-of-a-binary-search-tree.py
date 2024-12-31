# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.getPath(root, p.val)
        qPath = self.getPath(root, q.val)
        i, res = 0, None

        while i < len(pPath) and i < len(qPath):
            if pPath[i].val != qPath[i].val:
                break
            res = pPath[i]
            i += 1
            
        return res 

    def getPath(self, root, target):
        res = []
        def dfs(root, target, cur):
            if not root: return
            if root.val == target:
                cur.append(root)
                res.append(cur[:])
                return 

            cur.append(root)
            dfs(root.left, target, cur)
            cur.pop()

            cur.append(root)
            dfs(root.right, target, cur)
            cur.pop()

        dfs(root, target, [])
        return res[0]