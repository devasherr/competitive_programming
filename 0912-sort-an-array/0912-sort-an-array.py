class Solution:
    def merge(self, left, right):
        res = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    def sortArray(self, nums):
        if len(nums) < 2: return nums
        mid = len(nums) // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
