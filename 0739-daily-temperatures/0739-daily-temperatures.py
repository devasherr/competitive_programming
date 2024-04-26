class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, prev_idx = stack.pop()
                cur_idx = i

                res[prev_idx] = cur_idx - prev_idx

            stack.append((temperatures[i], i))

        return res