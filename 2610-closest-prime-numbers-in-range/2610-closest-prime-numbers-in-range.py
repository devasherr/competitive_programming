class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for _ in range(right+1)]
        primes[0], primes[1] = False, False

        for i in range(2, int(right ** 0.5) + 1):
            if primes[i]:
                j = i * i
                while j <= right:
                    primes[j] = False
                    j += i
        
        amount = float("inf")
        res = [-1, -1]

        for i in range(left, right + 1):
            if not primes[i]: continue

            while left < i:
                if primes[left] and primes[i] and i - left < amount:
                    res = [left, i]
                    amount = i - left
                left += 1
        
        return res