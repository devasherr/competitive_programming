class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for i in range(1, len(rating) - 1):
            left_smaller = 0
            right_larger = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller += 1
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    right_larger += 1 

            res += (left_smaller * right_larger)

            left_larger = i - left_smaller
            right_smaller = len(rating) - i - 1 - right_larger
            res += (left_larger * right_smaller)

        return res