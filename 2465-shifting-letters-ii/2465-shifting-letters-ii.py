class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0 for _ in range(len(s))]
        for shift in shifts:
            start, end, direction = shift
            startVal = 1 if direction == 1 else -1
            endVal = -1 if direction == 1 else 1

            changes[start] += startVal
            if end + 1 < len(changes):
                changes[end + 1] += endVal
        for i in range(1, len(changes)):
            changes[i-1] %= 26
            changes[i] += changes[i-1]
            changes[i] %= 26
        
        def convert(c, val):
            if val == 0: return c
            if val > 0:
                if ord(c) + val > ord("z"):
                    return chr(ord("a") + ((ord(c) + val - 1) - ord("z")))
                else:
                    return chr(ord(c) + val)
            if val < 0:
                if ord(c) + val < ord("a"):
                    diff = ord("a") - (ord(c) + val)
                    return chr(min(ord("z") - diff + 1, ord("z")))
                else:
                    return chr(ord(c) + val)

        res = []
        for i in range(len(s)):
            res.append(convert(s[i], changes[i]))
        return "".join(res)