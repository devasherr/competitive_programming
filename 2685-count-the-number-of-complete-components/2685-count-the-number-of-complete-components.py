class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node):
            q = deque([node])
            childCount = 0
            nodes = 0

            while q:
                cur = q.popleft()
                visit.add(cur)

                nodes += 1
                childCount += len(graph[cur])

                for child in graph[cur]:
                    if child in visit: continue
                    q.append(child)

            return nodes * (nodes - 1) == childCount

        res = 0
        for i in range(n):
            if i in visit: continue
            if bfs(i):
                res += 1

        return res + 1
