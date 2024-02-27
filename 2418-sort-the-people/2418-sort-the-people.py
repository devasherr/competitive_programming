class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        heightMap = {}
        
        # map heights with index
        for i in range(len(heights)):
            heightMap[heights[i]] = i

        # sort the heights
        for key in heightMap.keys():
            res.append(key)
        res.sort(reverse = True)

        # get names based on sorted height index
        for i in range(len(res)):
            res[i] = names[heightMap[res[i]]]
            
        return res