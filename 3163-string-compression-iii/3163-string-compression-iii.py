class Solution:
    def compressedString(self, word: str) -> str:
        word += "a" if word[-1] != "a" else "b"

        curCount, curWord = 0, word[0]
        res = []
        for i in range(len(word)):
            if curCount == 9 or word[i] != curWord:
                res.extend([str(curCount), curWord])
                curWord = word[i]
                curCount = 1
                continue
            
            curCount += 1
        
        return "".join(res)