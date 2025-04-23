class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digitCount(n):
            cur = 0
            while n:
                cur += n % 10
                n //= 10
            return cur

        count = defaultdict(int)
        mx = 0
        
        for i in range(1, n+1):
            val = digitCount(i)
            count[val] += 1 

            mx = max(mx, count[val])
        
        res = 0
        for _, val in count.items():
            if val == mx:
                res += 1
            
        return res