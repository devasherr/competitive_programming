class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for u, v in edges:
            count[u] += 1
            count[v] += 1
        
        for key in count:
            if count[key] == len(edges): return key