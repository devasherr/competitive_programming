class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorCount = defaultdict(int)

        res = []
        for query in queries:
            ball, color = query
            if ball in ballToColor:
                colorCount[ballToColor[ball]] -= 1
                if colorCount[ballToColor[ball]] == 0:
                    del colorCount[ballToColor[ball]]

            ballToColor[ball] = color
            colorCount[color] += 1
            res.append(len(colorCount))
        
        return res