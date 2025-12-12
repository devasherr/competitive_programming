# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def construct(self, head):
        cur = ListNode()
        tail = cur

        while head:
            tail.next = ListNode(head.val)
            tail = tail.next
            
            if not head.next or not head.next.next:
                break
            head = head.next.next

        return cur.next, tail

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode()
        tail = dummy

        h, t = self.construct(head)
        tail.next = h
        tail = t

        if head.next:
            h, t = self.construct(head.next)
            tail.next = h

        return dummy.next
