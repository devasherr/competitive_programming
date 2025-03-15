class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def findParent(x):
            if parent[x] == x: return x
            parent[x] = findParent(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = findParent(x), findParent(y)
            if px == py: return
            
            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += 1
            else:
                parent[px] = py
                rank[py] += 1

        for u, v in edges:
            union(u, v)

        return findParent(source) == findParent(destination)