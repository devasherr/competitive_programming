# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        tail = dummy

        while head:
            if head.val not in nums:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next

        return dummy.next
