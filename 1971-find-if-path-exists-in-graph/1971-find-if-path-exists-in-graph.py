class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node):
            if node == destination: return True
            visit.add(node)

            for child in graph[node]:
                if child not in visit:
                    if dfs(child):
                        return True
            
            return False
        
        return dfs(source)