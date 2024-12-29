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
        q = deque(data.split())
        def preOrder(q):
            if not q: return

            cur = q.popleft()
            if cur == "N": return
            node = TreeNode(int(cur))
            node.left = preOrder(q)
            node.right = preOrder(q)

            return node
        return preOrder(q)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))