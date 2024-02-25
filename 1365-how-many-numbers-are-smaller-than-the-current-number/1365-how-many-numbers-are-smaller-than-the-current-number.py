class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort and make index map
        indexMap = {}
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if not sorted_nums[i] in indexMap:
                indexMap[sorted_nums[i]] = i

        # make new res with index
        res = [indexMap[n] for n in nums]
        return res