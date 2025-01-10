class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2Count = Counter()
        for word in words2:
            curCount = Counter(word)
            for key in curCount:
                word2Count[key] = max(word2Count[key], curCount[key])

        res = []

        for word in words1:
            word1Count = Counter(word)
            good = True
            for key in word2Count:
                if word2Count[key] > word1Count[key]:
                    good = False
                    break
            if good:
                res.append(word)

        return res