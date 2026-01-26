class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)

        res = 0
        while len(heap) > 1:
            t1, t2 = heapq.heappop(heap), heapq.heappop(heap)

            t1 += 1
            t2 += 1

            if t1: heapq.heappush(heap, t1)
            if t2: heapq.heappush(heap, t2)

            res += 1

        return res
