class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        self.curMin = 1

    def popSmallest(self) -> int:
        if self.minHeap:
            return heapq.heappop(self.minHeap)
        else:
            self.curMin += 1
            return self.curMin - 1

    def addBack(self, num: int) -> None:
        if self.curMin > num:
            heapq.heappush(self.minHeap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)