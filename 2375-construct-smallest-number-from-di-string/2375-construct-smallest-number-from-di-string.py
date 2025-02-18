class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nums = set([i for i in range(1, n + 2)])
        idx = 0
        res = []

        while idx <= n:
            num = float("inf")
            for val in nums:
                num = min(num, val)
            if idx == n:
                res.append(num)
                break
            if pattern[idx] == "I":
                res.append(num)
                nums.remove(num)
                idx += 1
                continue

            j = idx
            count = 0
            while idx < len(pattern) and pattern[idx] == "D":
                count += 1
                idx += 1
            
            num += count
            while j != idx:
                res.append(num)
                nums.remove(num)
                num -= 1
                j += 1
                print(res)

        return "".join(map(str, res))