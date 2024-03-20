# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numsCount = defaultdict(int)
        cur = head

        while cur:
            numsCount[cur.val] += 1
            cur = cur.next

        cur = head
        dummy = ListNode()
        tail = dummy

        while cur:
            if numsCount[cur.val] == 1:
                tail.next = cur
                tail = tail.next
            else:
                tail.next = None
            cur = cur.next
            
        return dummy.next