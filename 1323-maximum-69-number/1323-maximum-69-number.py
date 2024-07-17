class Solution:
    def maximum69Number (self, num: int) -> int:
        n = 1
        prev = num
        while prev > 10:
            n *= 10
            prev //= 10

        res = 0
        f = 0
        while n:
            cur = (num // n) % 10
            n //= 10
            res *= 10
                
            if cur == 6 and not f:
                f = 1
                res += 9
                continue

            res += cur

        return res