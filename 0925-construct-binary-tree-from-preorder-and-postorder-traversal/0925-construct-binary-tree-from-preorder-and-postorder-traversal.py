# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexMap = {postorder[i]:i for i in range(len(postorder))}
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, len(preorder)):
            idx = indexMap[preorder[i]]
            while stack and indexMap[stack[-1].val] < idx:
                stack.pop()
            
            Node = TreeNode(preorder[i])
            if not stack[-1].left:
                stack[-1].left = Node
            else:
                stack[-1].right = Node
            stack.append(Node)
        
        return root