class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1

        lengthMap = defaultdict(int)
        lengthMap[1] = 1

        for i in range(1, len(dp)):
            touched = False
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    lengthMap[dp[j]+1] += 1
                else:
                    dp[i] = max(dp[i], 1)
                    touched = True
            if touched:
                lengthMap[1] += 1
        
        maxIndex = -1
        for key in lengthMap:
            maxIndex = max(maxIndex, key)
        
        return lengthMap[maxIndex]