class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countSet = set()

        for n in nums:
            if n in countSet:
                return True

            countSet.add(n)
        return False