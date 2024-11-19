class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        duplicates = set()
        curSum = 0

        for i in range(k-1):
            count[nums[i]] += 1
            curSum += nums[i]
            if count[nums[i]] > 1:
                duplicates.add(nums[i])
        
        res = 0
        for i in range(k-1, len(nums)):
            left, right = nums[i-k+1], nums[i]
            curSum += right
            count[right] += 1

            if count[right] > 1:
                duplicates.add(right)
            
            if not duplicates:
                res = max(res, curSum)
                
            count[left] -= 1
            curSum -= left
            if count[left] == 1:
                duplicates.remove(left)
        return res