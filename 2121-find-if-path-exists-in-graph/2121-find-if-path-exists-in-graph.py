class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visit = set()

        while q:
            node = q.popleft()
            visit.add(node)

            if node == destination:
                return True
            
            for child in graph[node]:
                if child not in visit:
                    q.append(child)
        
        return False