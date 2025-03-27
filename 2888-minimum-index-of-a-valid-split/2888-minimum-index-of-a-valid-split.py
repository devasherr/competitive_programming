class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        rightCount = Counter(nums)
        leftCount = defaultdict(int)

        dom = max(rightCount, key=rightCount.get)
        
        for i in range(len(nums)):
            leftCount[nums[i]] += 1
            rightCount[nums[i]] -= 1

            if leftCount[dom] > (i + 1) // 2  and rightCount[dom] > (len(nums) - i - 1) // 2:
                return i
        return -1