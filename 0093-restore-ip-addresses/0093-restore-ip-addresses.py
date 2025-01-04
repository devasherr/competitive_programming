class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()

        def validDigit(digit):
            if len(digit) > 1 and digit[0] == "0":
                return False
            if int(digit) > 255: return False
            return True

        def backtrack(i, addr):
            if i >= len(s):
                if len(addr) == 4:
                    res.add(".".join(addr))
                return
            
            for l in [1,2,3,4]:
                digit = s[i:i+l]
                if not validDigit(digit):
                    continue
                addr.append(digit)
                backtrack(i+l, addr)
                addr.pop()

        backtrack(0, [])
        return list(res)