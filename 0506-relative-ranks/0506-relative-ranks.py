class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxHeap = []
        for index, s in enumerate(score):
            # negative coz we only have min heap
            heapq.heappush(maxHeap, (-s, index))

        res = ["" for _ in range(len(score))]
        top = 1

        while maxHeap:
            originalIndex = heapq.heappop(maxHeap)[1]

            if top == 1:
                res[originalIndex] = "Gold Medal"
            elif top == 2:
                res[originalIndex] = "Silver Medal"
            elif top == 3:
                res[originalIndex] = "Bronze Medal"
            else:
                # if top 3 places are taken just add the number
                res[originalIndex] =  str(top)
            
            top += 1

        return res