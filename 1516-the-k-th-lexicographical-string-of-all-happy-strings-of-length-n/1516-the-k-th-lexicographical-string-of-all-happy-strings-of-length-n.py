class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.k = k
        def backtrack(cur):
            if len(cur) > n:
                return False
            if len(cur) > 1 and cur[-1] == cur[-2]:
                return False
            if len(cur) == n:
                self.k -= 1
                if self.k == 0:
                    return True
                return False
            
            for c in ["a", "b", "c"]:
                cur.append(c)
                if backtrack(cur):
                    return cur
                cur.pop()
        
        res = backtrack([])
        return "".join(res) if res else ""