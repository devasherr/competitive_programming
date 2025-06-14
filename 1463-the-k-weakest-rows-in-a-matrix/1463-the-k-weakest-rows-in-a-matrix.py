class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            s = 0
            for j in range(len(mat[0])):
                s += mat[i][j]
            heap.append((s, i))

        heapq.heapify(heap)
        res = []

        for _ in range(k):
            _, r = heapq.heappop(heap)
            res.append(r)
        
        return res