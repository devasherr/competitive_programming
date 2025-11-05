from collections import defaultdict

class Solution:
    def maxSubstrings(self, word: str) -> int:
        stack = []
        indexMap = {}
        res = 0

        for i in range(len(word)):
            if word[i] not in indexMap:
                stack.append(word[i])
                indexMap[word[i]] = i
                continue

            if i - indexMap[word[i]] < 3:
                continue

            while stack:
                val = stack.pop()
                del indexMap[val]

            res += 1

        return res
