class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for route in routes:
            graph[route[len(route)-1]].append(route[0])
            i = 0

            while i < len(route) - 1:
                graph[route[i]].append(route[i+1])
                i += 1
        
        q = deque([source])
        visited = set()
        res = 1
        found = False

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                if cur == target:
                    found = True
                    break

                for num in graph[cur]:
                    if num not in visited:
                        if len(graph[cur]) > 1:
                            res += 1
                        q.append(num)

        return res if found else -1