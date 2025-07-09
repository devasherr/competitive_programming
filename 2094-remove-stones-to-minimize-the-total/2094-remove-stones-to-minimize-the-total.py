class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        piles = [n*-1 for n in piles]
        heapq.heapify(piles)
        for _ in range(k):
            cur = heapq.heappop(piles)
            cur = math.ceil(cur // 2)
            if cur < 0:
                heapq.heappush(piles, cur)
        
        return sum(piles) * -1