class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyMap = {}
        i = 97

        for c in key:
            if c != " " and c not in keyMap:
                keyMap[c] = chr(i)
                i += 1

        res = ""
        for c in  message:
            if c == " ":
                res += " "
            else:
                res += keyMap[c]

        return res