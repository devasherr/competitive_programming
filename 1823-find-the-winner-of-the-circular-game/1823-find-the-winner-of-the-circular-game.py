class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # our players
        nums = [p for p in range(1, n + 1)]

        i = k - 1
        while len(nums) > 1:
            nums.pop(i)

            # circular traversal
            i = (i + k - 1) % len(nums)

        return nums[0]