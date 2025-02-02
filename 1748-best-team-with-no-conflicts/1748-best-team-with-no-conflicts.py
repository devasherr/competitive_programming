class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [[ages[i], scores[i]] for i in range(len(scores))]
        players.sort()

        print(players)
        def dp(i, maxScore):
            if i == len(scores):
                return 0
            if (i, maxScore) not in memo:
                include = 0
                if players[i][1] >= maxScore:
                    include = players[i][1] + dp(i+1, max(maxScore, players[i][1]))
                exclude = dp(i+1, maxScore)

                memo[(i, maxScore)] = max(include, exclude)
            return memo[(i, maxScore)]
        
        memo = {}
        return dp(0, 0)