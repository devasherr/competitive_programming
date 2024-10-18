class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        primes = [True for _ in range(n)]
        primes[0], primes[1] = False, False

        k = 2
        while k*k < n:
            if primes[k]:
                j = k * 2
                while j < n:
                    primes[j] = False
                    j += k
            k += 1
        
        count = 0
        for p in primes:
            count += p
        return count