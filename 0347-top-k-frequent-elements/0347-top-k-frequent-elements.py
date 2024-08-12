class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key in count:
            heap.append((-count, key))

        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        
        return res