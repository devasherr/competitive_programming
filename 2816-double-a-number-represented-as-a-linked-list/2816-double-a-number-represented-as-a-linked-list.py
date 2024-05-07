# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # double vals to new list considering carries
        cur = prev
        
        carry = 0
        dummy = ListNode()
        tail = dummy

        while cur or carry:
            val = (cur.val * 2) if cur else 0
            print(val)

            doubleVal = val % 10
            carry = val // 10

            
            tail.next = ListNode(doubleVal)
            tail = tail.next
            cur = cur.next

        return dummy.next