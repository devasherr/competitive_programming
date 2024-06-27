class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque()
        count, res = 0, [0 for i in range(n)]

        visited = set()
        redList = defaultdict(list)
        blueList = defaultdict(list)

        for u, v in redEdges:
            redList[u].append(v)
        for u, v in blueEdges:
            blueList[u].append(v)

        for node in redList[0]:
            q.append((node, 'red'))
        for node in blueList[0]:
            q.append((node, 'blue'))

        while q:
            count += 1
            for _ in range(len(q)):
                node, color = q.popleft()
                if not res[node]:
                    res[node] = count
                print(count)
                
                if color == 'red':
                    for num in blueList[node]:
                        if (num, 'blue') not in visited:
                            q.append((num, 'blue'))
                            visited.add((num, 'blue'))
                else:
                    for num in redList[node]:
                        if (num, 'red') not in visited:
                            q.append((num, 'red'))
                            visited.add((num, 'red'))
        
        for i in range(1, n):
            if res[i] == 0:
                res[i] = -1

        return res