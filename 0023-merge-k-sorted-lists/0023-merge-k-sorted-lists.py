# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for l in lists:
            cur = l
            while cur:
                vals.append(cur.val)
                cur = cur.next

        vals.sort(reverse=True)

        dummy = ListNode(0)
        tail = dummy

        while vals:
            node = ListNode(vals.pop())
            tail.next = node
            tail = tail.next

        return dummy.next
