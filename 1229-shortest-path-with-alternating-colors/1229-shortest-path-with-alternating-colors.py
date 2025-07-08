class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)

        for u, v in redEdges:
            redGraph[u].append(v)
        for u, v in blueEdges:
            blueGraph[u].append(v)

        def bfs(color):
            q = deque([(0, color)])
            visit = set((0, color))
            level = 0

            while q:
                for _ in range(len(q)):
                    node, color = q.popleft()
                    res[node] = min(res[node], level)

                    if color == 'r':
                        for child in blueGraph[node]:
                            if (child, 'b') not in visit:
                                q.append((child, 'b'))
                                visit.add((child, 'b'))
                    else:
                        for child in redGraph[node]:
                            if (child, 'r') not in visit:
                                q.append((child, 'r'))
                                visit.add((child, 'r'))
                level += 1

        res = [float("inf")] * n
        bfs('r')
        bfs('b')
        for i in range(n):
            if res[i] == float("inf"):
                res[i] = -1
        return res