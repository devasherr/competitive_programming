class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def fastExp(a, n):
            res = 1
            while n > 0:
                if n & 1:
                    res = (res * a) % MOD
                
                a = (a * a) %  MOD
                n >>= 1
            return res

        n = 0
        
        for v in b:
            n *= 10
            n += v
        
        return fastExp(a, n) % MOD