class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        idx = 1
        while idx < len(cardPoints):
            cardPoints[idx] += cardPoints[idx - 1]
            idx += 1
        
        # add a zero at the start
        cardPoints.insert(0, 0)
        print(cardPoints)

        res = cardPoints[k]

        left = k - 1 
        right = len(cardPoints) - 2

        while left >= 0:
            rightPortion = cardPoints[-1] - cardPoints[right]
            res = max(res, cardPoints[left] + rightPortion)
            left -= 1
            right -= 1

        return res