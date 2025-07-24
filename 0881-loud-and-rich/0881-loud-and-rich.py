class Solution:
    def loudAndRich(self, richer, quiet):
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        
        def dfs(node, val):
            if res[node] != -1: return [res[node], quiet[res[node]]]
            if graph[node] == []: return [node, quiet[node]]

            cur = [node, val]
            for child in graph[node]:
                child_node, child_val = dfs(child, quiet[child])
                if child_val < cur[1]:
                    cur = [child_node, child_val]
            
            res[node] = cur[0]
            return cur
        
        res = [-1 for i in range(len(quiet))] 
        for i in range(len(quiet)):
            if res[i] == -1:
                res[i] = dfs(i, quiet[i])[0]
        
        return res