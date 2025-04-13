class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def fastExp(n, p):
            res = 1
            while p > 0:
                if p & 1:
                   res = (res * n) % mod 
                n = (n * n) % mod
                p >>= 1

            return res

        odd, even = math.ceil(n/2), math.floor(n/2)
        a = fastExp(5, odd)
        b = fastExp(4, even)

        return (a * b) % mod