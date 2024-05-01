class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:  return 1
            if x == 0:  return 0

            res = helper(x ** 2, n // 2)
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        # a ^ -b == 1 / a ^ b
        return res if n >= 0 else 1/res