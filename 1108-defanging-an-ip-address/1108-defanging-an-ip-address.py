class Solution:
    def defangIPaddr(self, address: str) -> str:
        index = len(address)

        for c in address:
            if c == ".":
                address += "[.]"
            else:
                address += c

        return address[index:]