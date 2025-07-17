class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        turns = 0
        while target > 1:
            if maxDoubles == 0:
                turns += target - 1
                break
            if maxDoubles > 0 and target % 2 == 0:
                target /= 2
                maxDoubles -= 1
            else:
                target -= 1
            turns += 1

        return int(turns)