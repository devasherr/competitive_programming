class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        res = 0

        for num in answers:
            if count[num] > 0:
                count[num] -= 1 
                continue
            
            res += num + 1
            count[num] = num
        
        return res