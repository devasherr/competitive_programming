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
            digitsMap[key].append(n)
        
        res = -1
        for key in digitsMap:
            if len(digitsMap[key]) < 2:
                continue
            
            target = sorted(digitsMap[key], reverse=True)
            res = max(res, target[0] + target[1])
        
        return res