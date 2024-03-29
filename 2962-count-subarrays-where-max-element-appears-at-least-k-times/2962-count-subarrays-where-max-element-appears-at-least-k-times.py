class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count, res = 0, 0
        target = max(nums)

        left = 0
        
        for right in range(len(nums)):
            if nums[right] == target:
                count += 1

            while count > k or (count == k and  nums[left] != target):
                if nums[left] == target:
                    count -= 1
                left += 1
            
            if count == k:
                res += (left + 1)

        return res