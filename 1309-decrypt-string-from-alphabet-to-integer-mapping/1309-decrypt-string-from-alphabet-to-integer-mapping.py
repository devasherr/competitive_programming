class Solution:
    def freqAlphabets(self, s: str) -> str:
        wordMap = {}
        res = ""

        # dynamic hashmap :)
        for i in range(1, 27):
            mapKey = str(i)
            wordMap[mapKey] = chr(96 + i)

        n = len(s) - 1
        while n >= 0:
            if s[n] == "#":
                num = str(s[n- 2]) + str(s[n - 1])
                res += wordMap[num]
                n = n - 3
            else:
                res += wordMap[s[n]]
                n -= 1

        return res[::-1]