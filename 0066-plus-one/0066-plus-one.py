class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        i = len(digits) - 1

        while i >= 0 or carry:
            num = digits[i] if i >= 0 else 0
            num += carry

            res.append(num % 10)
            carry = num // 10
            i -= 1

        return reversed(res)