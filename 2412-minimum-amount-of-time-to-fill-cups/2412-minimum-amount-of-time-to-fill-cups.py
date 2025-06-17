class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        for i in range(len(amount)):
            if amount[i] == 0: continue
            heap.append(amount[i]*-1)

        heapq.heapify(heap)
        res = 0

        while heap:
            if len(heap) == 1:
                res += abs(heapq.heappop(heap))
                break
            
            x = heapq.heappop(heap) + 1
            y = heapq.heappop(heap) + 1

            res += 1
            if x: heapq.heappush(heap, x)
            if y: heapq.heappush(heap, y)

        return res