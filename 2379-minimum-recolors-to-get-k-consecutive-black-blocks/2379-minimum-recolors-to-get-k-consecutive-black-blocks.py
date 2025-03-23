class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = defaultdict(int)
        left, res = 0, len(blocks)
        
        for right in range(len(blocks)):
            count[blocks[right]] += 1

            if right - left == k - 1:
                res = min(res, count["W"])
                count[blocks[left]] -= 1
                left += 1
            
        return res