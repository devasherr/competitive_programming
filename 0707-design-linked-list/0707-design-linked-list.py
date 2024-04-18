class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(0, self.head)
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.head or self.size == 0:
            self.head = newNode
            return
        
        cur = self.head
        while cur and cur.next:
            cur = cur.next
            
        cur.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            newNode = ListNode(val)
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            
            temp = cur.next
            cur.next = newNode
            newNode.next = temp

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)