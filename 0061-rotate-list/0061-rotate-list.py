# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        tail = head
        length = 1

        while tail and tail.next:
            length += 1
            tail = tail.next
        
        k %= length
        
        if k == 0 or length == 1 or k == length:
            return head
        
        dummy = ListNode(0, head)
        cur = dummy
        for _ in range(length - k):
            cur = cur.next

        # connect the 
        newHead = cur.next
        cur.next = None

        tail.next = dummy.next
        dummy.next = newHead
        return dummy.next