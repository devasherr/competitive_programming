class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indexMap = {}
        for i in range(len(position)):
            indexMap[position[i]] = i
        position.sort()

        minSpeed = 0
        res = set()

        for i in range(len(position)-1, -1, -1):
            cur = (target - position[i]) / speed[indexMap[position[i]]]
            if cur > minSpeed:
                res.add(cur)
                
            minSpeed = max(minSpeed, cur)

        return len(res)