class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winCount, loseCount = Counter(), Counter()
        for match in matches:
            winCount[match[0]] += 1
            loseCount[match[1]] += 1

        win, one_lose = [], []
        for key in winCount:
            if loseCount[key] == 0:
                win.append(key)
        for key in loseCount:
            if loseCount[key] == 1:
                one_lose.append(key)

        return [sorted(win), sorted(one_lose)]
