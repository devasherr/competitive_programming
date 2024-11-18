# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        cur = head
        head = prev

        while cur and cur.next:
            temp = cur
            cur = cur.next

            temp.next = cur.next
            cur.next = temp
            prev.next = cur

            prev = temp
            cur = temp.next

        return head.next