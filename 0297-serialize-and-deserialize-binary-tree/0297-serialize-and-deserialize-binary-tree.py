# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root: return ""

        res = []
        q = deque([root])
        level = 1

        while q:
            good = False
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    # par
                    res.append(" null")
                    # child
                    q.append(None)
                    q.append(None)
                    continue
                good = True
                res.append(" "+str(node.val))

                q.append(node.left)
                q.append(node.right)         

            if not good: break
        return "".join(res)

    def deserialize(self, data):
        if not data: return None

        data = data.split()
        root = TreeNode(int(data[0]))
        q = deque([(root, 0)])

        while q:
            node, idx = q.popleft()
            leftIdx, rightIdx = 2*idx+1, 2*idx+2
            if leftIdx < len(data) and data[leftIdx] != "null":
                node.left = TreeNode(int(data[leftIdx]))
                q.append((node.left, leftIdx))
            if rightIdx < len(data) and data[rightIdx] != "null":
                node.right = TreeNode(int(data[rightIdx]))
                q.append((node.right, rightIdx))

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))