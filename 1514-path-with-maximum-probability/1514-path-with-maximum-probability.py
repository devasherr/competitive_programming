class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        visit = set()
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        self.res = 0
        def dfs(cur, calc):
            if cur == end_node:
                self.res = max(self.res, calc)
                return
            visit.add(cur)
            for child in graph[cur]:
                if child[0] not in visit:
                    dfs(child[0], calc*child[1])
            return 0

        dfs(start_node, 1)
        return self.res