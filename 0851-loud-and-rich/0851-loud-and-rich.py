class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        adjList = defaultdict(list)
        for x, y in richer:
            adjList[y].append(x)
        
        cache = defaultdict(lambda: None)
        def dfs(cur):
            if cache[cur]:
                return cache[cur]
            
            cache[cur] = cur
            for child in adjList[cur]:
                cand = dfs(child)
                if quiet[cand] < quiet[cache[cur]]:
                    cache[cur] = cand
            return cache[cur]

        res = [i for i in range(N)]
        for i in range(N):
            res[i] = dfs(i)
        return res