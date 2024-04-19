# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the lists
        def reverseList(lisst):
            prev = None
            cur = lisst

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            return prev

        l1 = reverseList(l1)
        l2 = reverseList(l2)

        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            tail.next = ListNode(val)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return reverseList(dummy.next)