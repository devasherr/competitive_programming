class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        numSet = [float("inf") for _ in range(n+1)]
        graph = defaultdict(list)
        for time in times:
            u, v, t = time
            graph[u].append((v, t))

        minHeap = [(0, k)]
        while minHeap:
            time, cur = heapq.heappop(minHeap)
            numSet[cur] = min(numSet[cur], time)  

            for child in graph[cur]:
                node, t = child
                if numSet[node] == float("inf"):
                    heapq.heappush(minHeap, (time+t, node))
        
        res = 0
        for num in numSet[1:]:
            if num == float("inf"): return -1
            res = max(res, num)
        return res