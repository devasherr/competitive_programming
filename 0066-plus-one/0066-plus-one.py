class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int("".join(map(str, digits)))
        s += 1
        return [int(c) for c in str(s)]