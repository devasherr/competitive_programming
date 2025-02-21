# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = set()
        self.traverse(root, 0)
    
    def traverse(self, root, val):
        self.vals.add(val)
        if root.left:
            self.traverse(root.left, val * 2 + 1)
        if root.right:
            self.traverse(root.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.vals        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)