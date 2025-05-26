class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i].sort()
            tup = (dominoes[i][0], dominoes[i][1])
            dominoes[i] = tup

        count = Counter(dominoes) 
        res = 0
        for c in count.values():
            n = c - 1
            res += n * (n + 1) // 2
        
        return res