# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()
        i = 0
        stack = [root]

        while i < len(traversal):
            cur = 0
            while i < len(traversal) and traversal[i] == "-":
                cur += 1
                i += 1
            
            while len(stack) > cur + 1:
                stack.pop()
            
            num = ""
            while i < len(traversal) and traversal[i] != "-":
                num += traversal[i]
                i += 1
            
            Node = TreeNode(int(num))
            if not stack[-1].left:
                stack[-1].left = Node
            else:
                stack[-1].right = Node
            stack.append(Node)

        return root.left     
