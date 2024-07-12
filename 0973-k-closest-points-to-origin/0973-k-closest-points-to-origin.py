class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p1, p2 in points:
            # no need for the whole formula
            dist = (p1**2) + (p2**2)
            minHeap.append([dist, p1, p2])

        heapq.heapify(minHeap)
        res = []

        while len(res) != k:
            dist, p1, p2 = heapq.heappop(minHeap)
            res.append([p1, p2])
        return res