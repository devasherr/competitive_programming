class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # 9,12,5,10,14,3,10
        res = []
        l = 0

        for n in nums:
            if n < pivot:
                res.insert(l, n)
                l += 1
            elif n > pivot:
                res.append(n)
            else:
                res.insert(l, n)
        return res