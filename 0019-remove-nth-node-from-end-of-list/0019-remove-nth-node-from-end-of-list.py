# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        for _ in range(n):
            # max base case here
            if not right.next:
                head = head.next
                return head
            right = right.next

        while right and right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return head
