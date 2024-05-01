class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        n = 1
        temp = [0, 1, 0]

        while n <= rowIndex:
            res = [0] * (n + 1)
            l, r = 0, 1

            while r < (n + 2):
                res[l] = temp[l] + temp[r]
                l += 1
                r += 1

            res = res
            temp = [0] + res + [0]

            n += 1

        return res