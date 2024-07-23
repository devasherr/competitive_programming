class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0

        while target > 1:
            if maxDoubles == 0:
                res += (target - 1)
                break

            if maxDoubles and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            res += 1
        
        return res