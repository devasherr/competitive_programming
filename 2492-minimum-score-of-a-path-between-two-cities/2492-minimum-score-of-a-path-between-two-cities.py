class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for road in roads:
            u, v, w = road
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        q = deque([1])
        visit = set()
        res = float("inf")

        while q:
            cur = q.popleft()

            for node in graph[cur]:
                child, weight = node
                res = min(res, weight)
                if child not in visit:
                    visit.add(child)
                    q.append(child)
        return res