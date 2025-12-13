class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = [n for n in nums if n < 0]
        i = 0
        while i < len(nums):
            if nums[i] >= 0: break
            i += 1

        res = []
        while len(res) != len(nums):
            if not neg:
                res.append(nums[i] * nums[i])
                i+=1
                continue
            if i == len(nums):
                n = neg.pop()
                res.append(n*n)
                continue

            if nums[i] < abs(neg[-1]):
                res.append(nums[i]*nums[i])
                i += 1
            else:
                n = neg.pop()
                res.append(n*n)

        return res
