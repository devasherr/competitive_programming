# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()

        s, b = less, more
        while head:
            newNode = ListNode(head.val)
            if head.val < x:
                s.next = newNode
                s = s.next
            else:
                b.next = newNode
                b = b.next

            head = head.next

        s.next = more.next
        return less.next
        