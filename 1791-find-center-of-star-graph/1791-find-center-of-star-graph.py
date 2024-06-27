class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeCount = defaultdict(int)

        for edge in edges:
            edgeCount[edge[0]] += 1
            edgeCount[edge[1]] += 1
        
        for key in edgeCount:
            if edgeCount[key] == len(edges):
                return key