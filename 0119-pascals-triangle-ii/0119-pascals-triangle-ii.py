class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = 1
        res = [1]
        temp = [0, 1, 0]

        while n <= rowIndex:
            cur = [0] * (n + 1)
            l, r = 0, 1

            while r < (n + 2):
                cur[l] = temp[l] + temp[r]
                l += 1
                r += 1

            res = cur
            temp = [0] + cur + [0]

            n += 1

        return res