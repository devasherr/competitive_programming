class Solution:
    def compress(self, chars: List[str]) -> int:
        left =  right = len(chars) - 1
        while left > 0:
            n = 0
            while chars[left] == chars[right]:
                n += 1
                left -= 1

            ten_thousand = n % 10
            thousand = (n // 10) % 10
            hundred = (n // 100) % 10
            ten = (n // 1000) % 10

            if ten_thousand > 0:
                chars[right] = str(ten_thousand)
                right -= 1
            if thousand > 0:
                chars[right] = str(thousand)
                right -= 1
            if hundred > 0:
                chars[right] = str(hundred)
                right -= 1
            if ten > 0:
                chars[right] = str(ten)
                right -= 1

            right = left
        
        left , right = 0, 1
        while left < len(chars) - 2:
            while chars[left] == chars[right]:
                chars.pop(right)

            left += 1
            right += 1

        return len(chars)