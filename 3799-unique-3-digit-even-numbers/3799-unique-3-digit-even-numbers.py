class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        self.res = set()
        def backtrack(n, depth, k):
            if depth > 3: return
            if k == 3 and n > 99 and n % 2 == 0:
                self.res.add(n)
                return

            for i in range(len(digits)):
                if i not in visit:
                    visit.add(i)
                    backtrack(n*10+digits[i], depth+1, k+1)
                    visit.remove(i)

                backtrack(n, depth+1, k)
        
        visit = set()
        backtrack(0, 0, 0)
        return len(self.res)