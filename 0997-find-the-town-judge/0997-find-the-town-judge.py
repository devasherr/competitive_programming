class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        notJudge = set()
        candidateJudge = defaultdict(int)

        for t in trust:
            notJudge.add(t[0])
            candidateJudge[t[1]] += 1
        
        for key in candidateJudge:
            if key not in notJudge and candidateJudge[key] == n -1:
                return key
        return -1