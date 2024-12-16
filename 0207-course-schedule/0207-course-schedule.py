class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node, visit):
            if node in visit: return False
            visit.add(node)

            for child in graph[node]:
                if not dfs(child, visit):
                    return False
            visit.remove(node)
            return True

        for i in range(numCourses):
            print(i)
            if not dfs(i, set()):
                return False
        return True