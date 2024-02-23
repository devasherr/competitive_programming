class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = []
        l = []
        winnerMap = defaultdict(int)
        loserMap = defaultdict(int)

        # winner and loser hashmap
        for m in matches:
            winnerMap[m[0]] += 1
            loserMap[m[1]] += 1

        # winner if not in loser
        for p in winnerMap:
            if p not in loserMap:
                w.append(p)

        # loser if count is 1
        for p in loserMap:
            if loserMap[p] == 1:
                l.append(p)

        # they have to be sorted
        w.sort()
        l.sort()
        
        return [w, l]