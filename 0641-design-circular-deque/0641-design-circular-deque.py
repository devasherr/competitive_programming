class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = deque()
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.count >= self.k:
            return False

        self.q.appendleft(value)        
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k:
            return False

        self.q.append(value)
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count >= 0:
            return False
        
        self.q.popleft()
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count <= 0:
            return False

        self.q.pop()
        self.count -= 1
        return True

    def getFront(self) -> int:
        return self.q[0] if self.q else -1

    def getRear(self) -> int:
        return self.q[-1] if self.q else -1

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.k else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()