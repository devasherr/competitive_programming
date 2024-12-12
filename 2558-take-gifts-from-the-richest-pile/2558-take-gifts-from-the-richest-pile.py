class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        
        for _ in range(k):
            cur = heapq.heappop(gifts)
            cur = math.floor(math.sqrt(abs(cur)))
            heapq.heappush(gifts, -cur)
        
        return sum(gifts) * -1