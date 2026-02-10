class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def permutation(arr, cur):
            if not arr:
                self.res.append(cur[::])
                return

            for i in range(len(arr)):
                cur.append(arr[i])
                permutation(arr[:i]+arr[i+1:], cur)
                cur.pop()

        permutation(nums, [])
        return self.res
