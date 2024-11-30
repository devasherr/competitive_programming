class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                graph[v].append(i)

        def bfs(cur):
            q = deque()
            q.append((cur, informTime[cur]))

            val = float("-inf")
            while q:
                for _ in range(len(q)):
                    node, time = q.popleft()
                    val = max(val, time)

                    for child in graph[node]:
                        q.append((child, time + informTime[child]))
            return val

        return bfs(headID)