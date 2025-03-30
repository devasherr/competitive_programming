class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightIndex = defaultdict(int)
        for i in range(len(s)):
            rightIndex[s[i]] = i
        
        prev, right = 0, 0
        res = []

        for left in range(len(s)):
            right = max(right, rightIndex[s[left]])
            if right == left:
                res.append(right - prev + 1)
                prev = right + 1
            
        return res