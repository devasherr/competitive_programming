class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        # calc left bound
        leftBound = [height[0] for h in height]
        lb = height[0]

        for i in range(1, N):
            leftBound[i] = lb
            lb = max(lb, height[i])

        # calc right bound
        rightBound = [height[-1] for h in height]
        rb = height[-1]

        for i in range(N - 2, -1, -1):
            rightBound[i] = rb
            rb = max(rb, height[i])

        # loop every elem in height
        res = 0
        for i in range(N):
            if height[i] < leftBound[i] and height[i] < rightBound[i]:
                res += min(leftBound[i], rightBound[i]) - height[i]

        return res