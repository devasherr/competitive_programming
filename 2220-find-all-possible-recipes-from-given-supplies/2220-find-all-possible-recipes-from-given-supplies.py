class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = defaultdict(list)
        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]

        def dfs(cur, visit):
            if not graph[cur]:
                return cur in supplies
            if cur in visit: return False
            
            visit.add(cur)
            for child in graph[cur]:
                if cur == child: return False
                if not dfs(child, visit):
                    return False
            visit.remove(cur)
            
            supplies.add(cur)
            return True

        res = []
        for r in recipes:
            if dfs(r, set()):
                res.append(r)
        
        return res