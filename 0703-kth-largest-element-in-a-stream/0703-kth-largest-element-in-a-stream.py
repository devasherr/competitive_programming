class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for n in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, n)
            else:
                self.addToHeap(n)
            
    def addToHeap(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        else:
            # add new element if val is less than top of the heap
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        self.addToHeap(val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)