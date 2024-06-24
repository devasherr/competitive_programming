class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False # loop detected
            if adjList[cur] == []:
                return True

            visit.add(cur)
            for pre in adjList[cur]:
                if not dfs(pre):
                    return False
            visit.remove(cur)
            # course resolved
            adjList[cur] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True