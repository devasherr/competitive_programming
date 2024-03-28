class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []

        # prefix sum
        x = sum(shifts)
        for i in range(len(s)):
            cur = ord(s[i]) - ord("a")
            rotate = (cur + x) % 26

            res.append(chr(ord("a") + rotate))
            
            # recompute prefix
            x = (x - shifts[i]) % 26

        return "".join(res)