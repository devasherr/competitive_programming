import sys
sys.set_int_max_str_digits(0)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # turn to number
        num = ""
        cur = head

        while cur:
            num += str(cur.val)
            cur = cur.next
        # double it

        num = str(int(num) * 2)
        # turn back to list
        dummy = ListNode()
        tail = dummy

        for n in num:
            tail.next = ListNode(int(n))
            tail = tail.next

        return dummy.next