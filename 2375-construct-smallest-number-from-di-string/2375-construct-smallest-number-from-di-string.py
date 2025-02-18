class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, tempStack = [], []

        for i in range(len(pattern) + 1):
            tempStack.append(i+1)

            while tempStack and (i == len(pattern) or pattern[i] == "I"):
                res.append(tempStack.pop())
            
        return "".join(map(str, res))