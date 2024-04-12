class Solution:
    def trap(self, height: List[int]) -> int:
        # get left max
        leftMax = [0] * len(height)
        curMax = 0
        for i in range(len(height)):
            leftMax[i] = curMax
            curMax = max(curMax, height[i])

        # get right max
        rightMax = [0] * len(height)
        curMax = 0
        for i in range(len(height) -1, -1, -1):
            rightMax[i] = curMax
            curMax = max(curMax, height[i])

        # find min from the left and right coz we are bound by the min
        combinedMin = [0] * len(height)
        for i in range(len(height)):
            combinedMin[i] = min(leftMax[i], rightMax[i])
            
        # subtract min from the height
        res = 0
        for i in range(len(height)):
            candidate = combinedMin[i] - height[i]
            if candidate > 0:
                res += candidate

        return res