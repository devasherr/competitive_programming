class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        res = ""
        # two stack for count and letters
        stringStack = []
        countStack = []

        # on ] remove from both stacks
        i = 0
        while i < n:
            if s[i].isdecimal():
                countStack.append(int(s[i]))
            elif s[i] == "[":
                i += 1
                continue
            elif s[i] == "]":
                k = countStack.pop()
                letter = stringStack.pop()

                val = ""
                for _ in range(k):
                    val += letter

                if stringStack:
                    stringStack[-1] += val
                else:
                    res += val
            else:
                cur = s[i]
                while i + 1 < n and ord("a") <= ord(s[i + 1]) <= ord("z"):
                    cur += s[i + 1]
                    i += 1
                stringStack.append(cur)
            i += 1

        if stringStack:
            res += stringStack.pop()

        return res