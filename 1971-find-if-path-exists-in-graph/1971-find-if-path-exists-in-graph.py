class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        childMap = defaultdict(list)

        for n, v in edges:
            childMap[n].append(v)

        q = deque([source])
        visited = [source]

        while q:
            node = q.popleft()
            if node == destination:
                return True

            for elem in childMap[node]:
                q.append(elem)

        return False