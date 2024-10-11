# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, list1, list2):
        newList = ListNode()
        tail = newList

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
        while list1:
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1 = list1.next
        while list2:
            tail.next = ListNode(list2.val)
            tail = tail.next
            list2 = list2.next
        return newList.next