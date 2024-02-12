class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for word in words:
            wordset = set(word.lower())
            if wordset <= row1 or wordset <= row2 or wordset <= row3:
                res.append(word)
        return res