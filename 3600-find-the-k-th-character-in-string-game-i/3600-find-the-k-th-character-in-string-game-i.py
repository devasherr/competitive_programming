class Solution:
    def kthCharacter(self, k: int) -> str:
        charMap = {}
        for i in range(26):
            j = 97 + i
            charMap[chr(j)] = chr(j+1)
        charMap[chr(25+97)] = 'a'
        
        def shift(w):
            res = []
            for c in w:
                res.append(charMap[c])
            return res

        w = ['a']
        while len(w) < k:
            w.extend(shift(w))
        return w[k-1]