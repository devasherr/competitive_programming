# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.next and head.val == head.next.val:
            head = head.next

        cur = head
        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            
            if cur:
                cur = cur.next 
        
        return head