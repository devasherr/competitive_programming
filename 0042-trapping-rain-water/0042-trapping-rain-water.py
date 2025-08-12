class Solution:
    def trap(self, height) -> int:
        n = len(height)
        leftMax = height[::]
        rightMax = height[::]

        # left prefix
        for i in range(1, n):
            leftMax[i] = max(leftMax[i], leftMax[i-1])
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i], rightMax[i+1])

        res = 0
        for i in range(1, n-1):
            res += max(min(leftMax[i-1], rightMax[i+1]) - height[i], 0)

        return res
