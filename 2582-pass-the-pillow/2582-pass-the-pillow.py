class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = time // (n - 1)
        step = time % (n - 1)

        if direction % 2 == 0:
            return step + 1

        return n - step