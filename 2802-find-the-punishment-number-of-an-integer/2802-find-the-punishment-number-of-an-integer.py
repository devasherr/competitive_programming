class Solution:
    def check(self, n: int) -> bool:
        num = list(str(n ** 2))
        def backtrack(i, cur):
            if i >= len(num):
                return cur == n

            window = len(num) - i
            for x  in range(1, window + 1):
                val = "".join(num[i:i+x])
                if backtrack(i+x, cur+int(val)):
                    return True
            return False
        
        return backtrack(0, 0)


    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if self.check(i):
                res += i ** 2
        return res