class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminder = [0] * k
        for n in arr:
            reminder[n%k] += 1
        
        if reminder[0] % 2 != 0:
            return False
        for i in range(1, (k // 2)+1):
            if reminder[i] != reminder[k-i]:
                return False
        return True