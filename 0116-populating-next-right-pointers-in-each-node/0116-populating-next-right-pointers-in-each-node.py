"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                nextNode = q[0] if q else None
                node.next = nextNode
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            node.next = None
        
        return root