class Solution:
    def rob(self, nums: List[int]) -> int:
        # if if odd and add 0
        # two pointers
        # compare
        if len(nums) % 2 != 0:
            nums.append(0)

        l, r = 0, 1
        lSum = 0
        rSum = 0

        while r <= len(nums) - 1:
            lSum += nums[l]
            rSum += nums[r]

            l += 2
            r += 2

        return max(lSum, rSum)