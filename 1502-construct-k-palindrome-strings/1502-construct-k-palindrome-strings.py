class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        count = Counter(s)
        oddCount, evenCount = 0, 0

        for key in count:
            if count[key] % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1

        if oddCount > k: return False
        return True