class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [] # [index, val]
        res = 0

        for i in range(len(heights)):
            while stack and stack[-1][1] > heights[i]:
                cur = stack.pop()

                leftLimit = stack[-1][0] if stack else -1
                rightLimit = i

                width = rightLimit - leftLimit - 1
                res = max(res, width * cur[1])

            stack.append([i, heights[i]])

        while stack:
            cur = stack.pop()
            leftLimit = stack[-1][0] if stack else -1

            width = len(heights) - leftLimit - 1
            res = max(res, width * cur[1])

        return res
