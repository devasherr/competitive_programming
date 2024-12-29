# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def preOrder(node):
            if not node:
                res.append(" N")
                return
            res.append(" "+str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)

        return "".join(res)

    def deserialize(self, data):
        data = data.split()
        self.idx = 0

        def preOrder():
            if self.idx >= len(data): return

            cur = data[self.idx]
            if cur == "N":
                self.idx += 1
                return 

            node = TreeNode(int(cur))
            self.idx += 1
            node.left = preOrder()
            node.right = preOrder()

            return node

        return preOrder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))