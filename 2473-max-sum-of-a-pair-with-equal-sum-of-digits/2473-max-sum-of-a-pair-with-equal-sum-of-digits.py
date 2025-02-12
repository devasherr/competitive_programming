class Solution:
    def calcSum(self, n):
        cur = 0
        while n:
            cur += (n % 10)
            n //= 10
        return cur

    def maximumSum(self, nums: List[int]) -> int:
        digitsMap = defaultdict(list)
        for n in nums:
            key = self.calcSum(n)
            if len(digitsMap[key]) < 2:
                digitsMap[key].append(n)
            else:
                if n < digitsMap[key][0] and n < digitsMap[key][1]:
                    continue
                if digitsMap[key][0] < digitsMap[key][1]:
                    digitsMap[key][0] = n
                else:
                    digitsMap[key][1] = n
        
        res = -1
        for key in digitsMap:
            if len(digitsMap[key]) < 2:
                continue
            res = max(res, digitsMap[key][0] + digitsMap[key][1])        
        return res