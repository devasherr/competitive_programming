class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        degree = [0 for _ in range(n)]
        rank = [0 for _ in range(n)]
        parent = [i for i in range(n)]

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] > rank[py]:
                parent[py] = px    
                rank[px] += 1
            else:
                parent[px] = py
                rank[py] += 1
        
        for u, v in edges:
            union(u, v)

        parent = [find(x) for x in parent]
        res = set(parent)
        ans = 0

        for val in res:
            nodes, edges = 0, 0

            for i in range(n):
                if parent[i] == val:
                    nodes += 1
                    edges += degree[i]

            edges = edges // 2
            if edges == nodes * (nodes - 1) // 2:
                ans += 1

        return ans