class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerMap, loserMap = {}, {}

        for winner, loser in matches:
            loserMap[loser] = loserMap.get(loser, 0) + 1
            winnerMap[winner] = winnerMap.get(winner, 0) + 1

        goats = []
        for key in winnerMap:
            if loserMap.get(key, 0) == 0:
                goats.append(key)
            
        averages = []
        for key in loserMap:
            if loserMap[key] == 1:
                averages.append(key)
        
        return [sorted(goats), sorted(averages)]