class Solution:
    def findMaxLength(self, nums):
        hashmap = {0: -1}
        zeros, ones, maxLen = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = zeros - ones
            if diff in hashmap:
                maxLen = max(maxLen, i - hashmap[diff])
            else:
                hashmap[diff] = i
        
        return maxLen