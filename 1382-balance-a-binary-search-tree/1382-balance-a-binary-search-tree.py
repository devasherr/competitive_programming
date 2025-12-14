# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root):
        #traverse the bst (inorder) and poppulate a list
        traversed = []
        def traverse(node):
            if not node: return
            
            traverse(node.left)
            traversed.append(node.val)
            traverse(node.right)
        traverse(root)

        print(traversed)
        #construct  la new balanced bst from that list
        def construct(lst):
            if not lst:
                return None
            mid = len(lst)//2
            ntree = TreeNode(lst[mid])
            ntree.left = construct(lst[:mid])
            ntree.right = construct(lst[mid+1:])
            return ntree    

        return construct(traversed)