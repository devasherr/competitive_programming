class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for _ in range(k):
            cur = heapq.heappop(nums)
        
        return cur * -1