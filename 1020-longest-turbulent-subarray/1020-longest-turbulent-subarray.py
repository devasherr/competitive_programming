class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        signs = []
        for i in range(1, len(arr)):
            sign = "="
            if arr[i-1] > arr[i]:
                sign = ">"
            elif arr[i-1] < arr[i]:
                sign = "<"
            signs.append(sign)
        
        res, cur = 0, 0
        idx = 0
        while idx < len(signs) and signs[idx] == "=":
            idx += 1
        sign = "="
        for i in range(idx, len(signs)):
            if signs[i] == "=":
                cur = 0
                continue
            if sign == "=":
                sign = "<" if signs[idx] == ">" else ">"

            if sign == signs[i]:
                cur = 1
                continue
            cur += 1
            sign = signs[i]

            res = max(res, cur)
        return res + 1
