import heapq
class Solution:
    def calc(self, x):
        res = 0
        while x != 1:
            if x & 1:
                x = 3 * x +1
            else:
                x = x // 2
            res += 1
        return res

    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for n in range(lo, hi+1):
            heap.append((self.calc(n), n))
        heapq.heapify(heap)

        res = -1
        for _ in range(k):
            _, org = heapq.heappop(heap)
            res = org
        return res
