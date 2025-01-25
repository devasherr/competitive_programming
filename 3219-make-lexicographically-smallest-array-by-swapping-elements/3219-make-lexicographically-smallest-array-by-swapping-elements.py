class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sortedNums = sorted(nums)

        numToGroup, groupElements = {sortedNums[0]: 0}, defaultdict(deque)
        groupElements[0].append(sortedNums[0])
        groupId = 0

        for i in range(1, len(sortedNums)):
            if abs(sortedNums[i] - sortedNums[i-1]) > limit:
                groupId += 1
            
            groupElements[groupId].append(sortedNums[i])
            numToGroup[sortedNums[i]] = groupId

        res = []
        for n in nums:
            idx = numToGroup[n]
            res.append(groupElements[idx].popleft())
        
        return res