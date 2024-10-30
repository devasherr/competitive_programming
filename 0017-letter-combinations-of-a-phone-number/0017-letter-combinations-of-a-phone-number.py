class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        def backtrack(i, cur):
            if i == len(digits):
                if cur: res.append(cur[:])
                return

            for c in numberMap[digits[i]]:
                cur.append(c)      
                backtrack(i+1, cur)
                cur.pop()
        
        backtrack(0, [])
        return ["".join(word) for word in res]