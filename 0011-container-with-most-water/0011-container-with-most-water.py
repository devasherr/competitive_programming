class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height)-1
        res = 0

        while left < right:
            cur = (right - left) * min(height[left], height[right])
            res = max(res, cur)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
