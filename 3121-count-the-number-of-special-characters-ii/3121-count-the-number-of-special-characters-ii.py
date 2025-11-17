class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        smallChar, upperChar = defaultdict(int), defaultdict(int)
        for i in range(len(word)):
            if word[i].islower():
                smallChar[word[i]] = i
            else:
                if word[i] not in upperChar:
                    upperChar[word[i]] = i

        res = 0
        for key in smallChar.keys():
            if smallChar[key] < upperChar[key.upper()]:
                res += 1

        return res
