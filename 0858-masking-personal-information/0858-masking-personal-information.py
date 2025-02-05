class Solution:
    def handleEmail(self, email):
        res = [email[0].lower(), "*****"]
        prev = email[0]
        for i in range(1, len(email)):
            if email[i] == "@":
                res.append(prev.lower())
                res.append(email[i])
                break
            prev = email[i]
        i += 1
        while i < len(email):
            res.append(email[i].lower())
            i += 1
        return "".join(res)

    def handlePhone(self, phone):
        res = []
        count = 0
        for i in range(len(phone) - 1, -1, -1):
            if phone[i].isalnum():
                if len(res) < 4:
                    res.append(phone[i])
                count += 1
        res.append("-***-***")
        if count == 11:
            res.append("-*+")
        if count == 12:
            res.append("-**+")
        if count == 13:
            res.append("-***+")

        return "".join(res)[::-1]

    def maskPII(self, s: str) -> str:
        for c in s:
            if c == "@":
                return self.handleEmail(s)
        return self.handlePhone(s)