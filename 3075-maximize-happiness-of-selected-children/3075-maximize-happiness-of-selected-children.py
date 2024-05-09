class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        cur = 0

        while k > 0:
            val = happiness.pop() - cur
            if val > 0:
                res += val

            k -= 1
            cur += 1

        return res