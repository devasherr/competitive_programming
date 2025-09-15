# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l2: return l1
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n, interval*2):
                firstHalf = lists[i]
                secondHalf = lists[i+interval] if i + interval < n else []
                lists[i] = self.mergeTwoLists(firstHalf, secondHalf)
            interval *= 2

        return lists[0]
