class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [] # (val, index)
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                val, index = stack.pop()
                res[index] = i - index
            
            stack.append((temperatures[i], i))

        return res
