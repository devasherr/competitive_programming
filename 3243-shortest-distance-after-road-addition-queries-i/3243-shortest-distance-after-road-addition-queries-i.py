class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n):
            graph[i].append(i+1)
        
        def search(num):
            q = deque([num])
            count = 0

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur == n - 1:
                        return count
                    
                    for child in graph[cur]:
                        q.append(child)
                count += 1

        res = []
        for u, v in queries:
            graph[u].append(v)
            res.append(search(0))
        
        return res