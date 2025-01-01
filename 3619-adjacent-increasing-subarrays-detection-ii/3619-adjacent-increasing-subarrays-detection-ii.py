class Solution:
    def calc(self, prefix, k):
        for left in range(len(prefix)):
            right = left + k
            if right + k - 1 == len(prefix):
                return False
            
            if prefix[left + k - 1] - prefix[left] == k - 1 and prefix[right + k - 1] - prefix[right] == k - 1:
                return True

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prefix = [1]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] + 1)
                
        left, right = 1, len(nums) // 2
        res = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            val = self.calc(prefix, mid)
            if val:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res