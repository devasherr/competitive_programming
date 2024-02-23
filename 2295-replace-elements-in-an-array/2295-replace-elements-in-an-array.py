class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # map of index
        indexMap = {}
        for i in range(len(nums)):
            indexMap[nums[i]] = i 
        
        # while replacing, keep track of the map
        for op in operations:
            nums[indexMap[op[0]]] = op[1]
            indexMap[op[1]] = indexMap[op[0]]
        return nums