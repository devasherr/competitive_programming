class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)

        edgeList = set()
        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 1 and (j, i) not in edgeList:
                        edgeList.add((i, j))

        edgeList = list(edgeList)

        parent = [i for i in range(N)]
        rank = [1] * N

        def findParent(n):
            res = n
            while res != parent[res]:
                res = parent[res]
            return res

        def union(n1, n2):
            # get parents
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            return 1

        res = N
        for n1, n2 in edgeList:
            res -= union(n1, n2)
        return res