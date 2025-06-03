class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(openCount, closeCount, path):
            if not openCount and not closeCount:
                res.append("".join(path))
                return
            if openCount > 0: 
                path.append("(")
                generate(openCount-1, closeCount, path)
                path.pop()
    
            if openCount < closeCount:
                path.append(")")
                generate(openCount, closeCount-1, path)
                path.pop()
        generate(n, n, [])
        return res
            