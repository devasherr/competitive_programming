class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        forward = True

        for _ in range(time):
            if forward:
                i += 1
            else:
                i -= 1
            
            if i == 1:
                forward = True
            if i == n:
                forward = False
        
        return i