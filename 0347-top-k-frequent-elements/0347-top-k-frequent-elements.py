class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)

        cur = [(val, key) for key, val in count.items()]
        cur.sort(reverse=True)

        res = [cur[i][1] for i in range(k)]
        return res