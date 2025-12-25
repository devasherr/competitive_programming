class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res, wait = 0, 0

        for i in range(k):
            res += max(happiness[i] - wait, 0)
            wait += 1

        return res


