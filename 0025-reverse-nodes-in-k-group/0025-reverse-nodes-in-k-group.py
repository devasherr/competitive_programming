# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # a -> b -> c -> d -> e == 3
        # x -> y == 3

        cur = head
        while cur:
            temp = ListNode()
            temp_tail = temp

            full = True
            for _ in range(k):
                if not cur:
                    full = False
                    break

                temp_tail.next = ListNode(cur.val)
                temp_tail = temp_tail.next
                cur = cur.next

            if full:
                rev = self.reverseList(temp.next)
                tail.next = rev
            else:
                tail.next = temp.next

            # i don't like this part
            while tail and tail.next:
                tail = tail.next

        return dummy.next
