# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        end = list1
        tail = list2
        for i in range(a - 1):
            start = start.next
        for i in range(b):
            end = end.next

        while tail and tail.next:
            tail = tail.next

        tail.next = end.next
        start.next = list2

        return list1