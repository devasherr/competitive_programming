# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        cur = head

        while cur and cur.next:
            next = cur.next
            s = 0
            while next and next.val != 0:
                s += next.val
                next = next.next

            tail.next = ListNode(s)
            tail = tail.next
            cur = next

        return dummy.next