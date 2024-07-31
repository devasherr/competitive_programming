class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for course, pre in prerequisites:
            adjList[pre].append(course)
        
        visit = set()
        def dfs(curCourse):
            if curCourse in visit:
                return False
            if adjList[curCourse] == []:
                return True

            visit.add(curCourse)
            for nei in adjList[curCourse]:
                if not dfs(nei):
                    return False
            
            
            adjList[curCourse] = []
            return True
        
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return False
        return True