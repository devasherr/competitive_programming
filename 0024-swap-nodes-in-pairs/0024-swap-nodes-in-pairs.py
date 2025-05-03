# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        cur = head
        while cur and cur.next:
            tail.next = ListNode(cur.next.val)
            tail = tail.next

            tail.next = ListNode(cur.val)
            cur = cur.next.next
            tail = tail.next

        while cur:
            tail.next = ListNode(cur.val)
            tail = tail.next
            cur = cur.next
        
        return dummy.next