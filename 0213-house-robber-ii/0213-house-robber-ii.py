class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helpRob(houses):
            two, one= 0, 0

            for i in range(len(houses)):
                temp = one
                one = max(one, two+houses[i])
                two = temp
            
            return one
        
        return max(helpRob(nums[:len(nums)-1]), helpRob(nums[1:]))