class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float("-inf")
        heap = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                res = max(res, x + y - (heap[0][0]))

            heapq.heappush(heap, (-(y-x), x))

        return res
