class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = self.generateKey(word)
            anagrams[key].append(word)

        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res
    
    def generateKey(self, word):
        count = [0 for _ in range(26)]
        for c in word:
            count[ord(c) - ord("a")] += 1
        return "*".join([str(c) for c in count])