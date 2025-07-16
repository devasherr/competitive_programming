class Solution:
    def lemonadeChange(self, bills) -> bool:
        count = {20: 0, 10: 0, 5: 0}

        for b in bills:
            n = b - 5
            for key in count:
                while count[key] and n - key >= 0:
                    n -= key
                    count[key] -= 1
            count[b] += 1
            if n != 0: return False

        return True