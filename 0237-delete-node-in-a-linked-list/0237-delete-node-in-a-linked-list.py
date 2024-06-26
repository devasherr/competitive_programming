# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # copy the next node
        nextNode = node.next
        node.val = nextNode.val
        
        # kill the next node
        node.next = node.next.next