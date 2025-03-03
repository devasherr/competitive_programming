class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        pc = 0
        for n in nums:
            if n < pivot:
                res.append(n)
            elif n == pivot:
                pc += 1
        for _ in range(pc):
            res.append(pivot)

        for n in nums:
            if n > pivot:
                res.append(n)

        return res 