class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = abs(heapq.heappop(stones))
            s2 = abs(heapq.heappop(stones))

            remain = s2 - s1
            if remain:
                heapq.heappush(stones, -remain)
        
        if not stones:
            return 0
        return abs(stones[0])