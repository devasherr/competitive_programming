class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-n for n in piles]
        heapq.heapify(piles)

        for _ in range(k):
            num = abs(heapq.heappop(piles))
            num -= (num // 2)
            heapq.heappush(piles, -num)
        
        return abs(sum(piles))