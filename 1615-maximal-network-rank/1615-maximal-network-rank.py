class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in roads:
            adjList[u].append(v)
            adjList[v].append(u)

        def generateSet(tempSet, key, vals):
            for v in vals:
                if (key, v) not in tempSet and (v, key) not in tempSet:
                    tempSet.add((key, v))
            return tempSet
        def removeSet(tempSet, key, vals):
            for v in vals:
                if (key, v) in tempSet:
                    tempSet.remove((key, v))
            return tempSet

        res = 0
        for i in range(n):
            temp = generateSet(set(), i, adjList[i])

            for j in range(i+1, n):
                temp = generateSet(temp, j, adjList[j])
                res = max(res, len(temp))
                temp = removeSet(temp, j, adjList[j])
                
            temp.clear()

        return res