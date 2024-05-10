class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heappush(minHeap, (arr[i]/ arr[j], [arr[i], arr[j]]))
        

        while k > 1:
            heappop(minHeap)
            k -= 1

        return heappop(minHeap)[1]