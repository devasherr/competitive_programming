class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sOne = "".join(word1)
        sTwo = "".join(word2)

        return sOne == sTwo