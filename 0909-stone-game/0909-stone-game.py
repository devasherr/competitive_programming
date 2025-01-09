class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(i, j):
            if i > j: return 0

            if (i, j) not in memo:
            # turn for alice if is count of elements is even
                alice = (j + i + 1) % 2 == 0
                left = piles[i] if alice else 0
                right = piles[j] if alice else 0

                memo[(i, j)] = max(left + dp(i+1, j), right + dp(i, j-1))
            return memo[(i, j)]

        memo = {}
        return dp(0, len(piles) -1) > sum(piles) // 2