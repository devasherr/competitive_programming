class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v, w = edges[i][0], edges[i][1], succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        maxHeap = [(-1, start_node)]
        visit = set()

        while maxHeap:
            prob, cur = heapq.heappop(maxHeap)
            visit.add(cur)

            if cur == end_node: return -prob
            for child in graph[cur]:
                if child[0] not in visit:
                    heapq.heappush(maxHeap, (child[1] * prob, child[0]))
        return 0