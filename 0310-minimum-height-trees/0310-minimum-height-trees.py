class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        treeMap = defaultdict(list)

        for pre, post in edges:
            treeMap[pre].append(post)
            treeMap[post].append(pre)
        
        for node in treeMap:
            if len(treeMap[node]) > 1:
                res.append(node)
        
        return res