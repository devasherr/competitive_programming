class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # hello
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        
        for _ in range(k):
            heapq.heappush(gifts, -math.floor(math.sqrt(abs(heapq.heappop(gifts)))))
        
        return sum(gifts) * -1