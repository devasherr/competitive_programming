class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        indexMap = defaultdict(list)
        mx_r, mx_c = -1, -1
        for i in range(len(nums)):
            mx_r = max(mx_r, i)
            for j in range(len(nums[i])):
                indexMap[i+j].append(nums[i][j])
                mx_c = max(mx_c, j)
        
        res = []
        for i in range(mx_r + mx_c + 1):
            for elem in indexMap[i][::-1]:
                res.append(elem)
        
        return res