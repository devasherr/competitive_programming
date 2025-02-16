class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0 for _ in range(2*n - 1)]
        visit = set()
        def backtrack(i):
            if len(visit) == n:
                return True
            
            for x in reversed(range(1, n+1)):
                if x in visit: continue
                if res[i] != 0 or (x != 1 and (i+x >= len(res) or res[i+x] != 0)):
                    continue
                
                res[i] = x
                if x != 1:
                    res[i+x] = x
                visit.add(x)
                
                j = i
                while j < len(res) and res[j] != 0:
                    j += 1

                if backtrack(j):
                    return True
                
                res[i] = 0
                if x != 1:
                    res[i+x] = 0
                visit.remove(x)
        
        backtrack(0)
        return res