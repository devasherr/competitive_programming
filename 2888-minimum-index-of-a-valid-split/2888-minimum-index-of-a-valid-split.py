class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        rightCount = Counter(nums)
        leftCount = defaultdict(int)

        dom, domCount = 0, 0
        for key in rightCount:
            if rightCount[key] > domCount:
                dom = key
                domCount = rightCount[key]
        
        for i in range(len(nums)):
            leftCount[nums[i]] += 1
            rightCount[nums[i]] -= 1

            if leftCount[dom] > (i + 1) // 2  and rightCount[dom] > (len(nums) - i - 1) // 2:
                return i
        return -1