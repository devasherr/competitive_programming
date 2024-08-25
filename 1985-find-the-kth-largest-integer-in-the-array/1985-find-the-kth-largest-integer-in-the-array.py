class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = [int(c) for c in nums]
        n.sort(reverse = True)

        return str(n[k - 1])