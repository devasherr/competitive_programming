class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)

        i = 0
        for n in [0, 1, 2]:
            for _ in range(count[n]):
                nums[i] = n
                i += 1