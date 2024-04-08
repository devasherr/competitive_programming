class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelSet = set(["a", "e", "i", "o", "u"])
        res = []

        wordsInNum = [0] * (len(words) + 1)
        for i in range(len(words)):
            if len(words[i]) > 0 and words[i][0] in vowelSet and words[i][-1] in vowelSet:
                wordsInNum[i + 1] += 1

        i = 1
        while i < len(wordsInNum):
            wordsInNum[i] += wordsInNum[i - 1]
            i += 1

        for query in queries:
            left, right = query
            res.append(wordsInNum[right + 1] - wordsInNum[left])

        return res