class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = []
        tl = []

        for c in s:
            if c == "#":
                # backspace of empty string is empty string
                if len(sl) == 0:
                    continue
                sl.pop()
            else:
                sl.append(c)

        for c in t:
            if c == "#":
                # backspace of empty string is empty string
                if len(tl) == 0:
                    continue
                tl.pop()
            else:
                tl.append(c)

        return sl == tl