"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        nodeMap = {}
        cur = head
        while cur:
            new_node = Node(cur.val)
            nodeMap[cur] = new_node
            cur = cur.next

        cur = head
        while cur:
            new_node = nodeMap[cur]
            new_node.next = nodeMap[cur.next] if cur.next in nodeMap else None
            new_node.random = nodeMap[cur.random] if cur.random in nodeMap else None
            cur = cur.next

        return nodeMap[head]
