class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        champ = [True for _ in range(n)]

        def bfs(node):
            q = deque([node])
            while q:
                curNode = q.popleft()
                for child in graph[curNode]:
                    if champ[child]:
                        q.append(child)
                        champ[child] = False

        for i in range(n):
            if champ[i]:
                bfs(i)
        
        res = -1
        for i in range(n):
            if champ[i]:
                if res != -1:
                    return -1
                res = i
        return res