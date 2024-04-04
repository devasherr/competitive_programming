class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, res = 0, 0
        count = defaultdict(int)

        for right in range(len(answerKey)):
            count[answerKey[right]] += 1

            while count["T"] > k and count["F"] > k:
                count[answerKey[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res