class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]
        prefix = [1]
        for i in range(1, len(colors)):
            val = 1 if colors[i] != colors[i-1] else 0
            prefix.append(prefix[-1] + val)

        left, res = 0, 0
        for right in range(k-1, len(colors)):
            if prefix[right] - prefix[left] + 1 == k:
                res += 1
            left += 1
            
        return res