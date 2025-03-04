class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(k):
            if k == 0: return True
            if k < 0: return False
            if k in memo:
                return memo[k]

            found = False
            for i in range(17):
                if i not in visit:
                    visit.add(i)
                    found = backtrack(k - (3**i))
                    if found: return True
                    visit.remove(i)
                
            memo[k] = found
            return memo[k]
        
        memo, visit = {}, set()
        return backtrack(n)