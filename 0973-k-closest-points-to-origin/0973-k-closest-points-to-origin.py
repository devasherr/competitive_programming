class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y):
            return ((x**2) + (y**2)) **0.5

        distMap = defaultdict(list)
        heap = []
        for p1, p2 in points:
            distance = getDistance(p1, p2)

            distMap[distance].append((p1, p2)) 
            heapq.heappush(heap, distance)
        
        res = []
        while len(res) != k:
            cur = heapq.heappop(heap)
            for val in distMap[cur]:
                res.append(val)

        return res