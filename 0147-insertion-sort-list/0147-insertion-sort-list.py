# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            node = head.val
            head = head.next
            cur = dummy

            while cur and cur.next:
                if node < cur.next.val:
                    break
                cur = cur.next

            prev = cur.next
            cur.next = ListNode(node, prev)

        return dummy.next