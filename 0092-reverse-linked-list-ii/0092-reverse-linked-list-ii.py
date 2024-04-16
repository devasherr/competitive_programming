# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        cur = head

        while cur:
          arr.append(cur.val)
          cur = cur.next

        # make zero indexed
        left -= 1
        right -= 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        cur = head

        for i in range(len(arr)):
            cur.val = arr[i]
            cur = cur.next
        
        return head