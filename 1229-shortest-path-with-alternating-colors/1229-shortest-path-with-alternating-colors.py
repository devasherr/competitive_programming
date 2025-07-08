class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)

        for u, v in redEdges:
            redGraph[u].append(v)
        for u, v in blueEdges:
            blueGraph[u].append(v)

        def bfs(target, path):
            q = deque([(0, path)])
            visit = set((0, path))
            level = 0

            while q:
                for _ in range(len(q)):
                    node, color = q.popleft()
                    if node == target: return level

                    if color == 'r':
                        for child in blueGraph[node]:
                            if (child, 'b') not in visit:
                                q.append((child, 'b'))
                                visit.add((child, 'b'))
                    if color == 'b':
                        for child in redGraph[node]:
                            if (child, 'r') not in visit:
                                q.append((child, 'r'))
                                visit.add((child, 'r'))
                level += 1  
            return float("inf")


        res = []
        for i in range(n):
            val = min(bfs(i, 'r'), bfs(i, 'b'))
            res.append(val if val != float("inf") else -1)
        return res