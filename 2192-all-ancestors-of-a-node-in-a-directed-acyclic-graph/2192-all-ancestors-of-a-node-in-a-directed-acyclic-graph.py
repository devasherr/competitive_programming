class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # topo sort
        indegreeList = [0 for _ in range(n)]
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            indegreeList[v] += 1

        q = deque()
        for i in range(n):
            if indegreeList[i] == 0:
                q.append(i)
        
        ancestors = [set() for _ in range(n)]
        while q:
            cur = q.popleft()

            for nei in adjList[cur]:
                ancestors[nei].add(cur)
                # union or combine the current result
                ancestors[nei] |= ancestors[cur]

                indegreeList[nei] -= 1
                if indegreeList[nei] == 0:
                    q.append(nei)
        return ancestors