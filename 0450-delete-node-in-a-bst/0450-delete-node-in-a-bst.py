# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # found the node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # find min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val

            # delete the duplicate node
            root.right = self.deleteNode(root.right, cur.val)
        return root