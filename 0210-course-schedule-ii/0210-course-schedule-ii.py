class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        inDegree = [0] * numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for child in graph[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    q.append(child)
        
        if len(res) != numCourses: return []
        return res