class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indergreeList = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indergreeList[a] += 1
        
        orderedList = []
        q = deque()
        for i in range(numCourses):
            if indergreeList[i] == 0:
                q.append(i)
            
        while q:
            cur = q.popleft()
            orderedList.append(cur)

            for child in graph[cur]:
                indergreeList[child] -= 1
                if indergreeList[child] == 0:
                    q.append(child)
        
        return orderedList if len(orderedList) == numCourses else []