class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1

        # start from one and check up until we find the number
        
        while True:
            if i % 2 == 0 and i % n == 0:
                return i
            i += 1
             