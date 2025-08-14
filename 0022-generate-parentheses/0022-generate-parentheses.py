class Solution:
    def generateParenthesis(self, n: int):
        self.res = []
        def generate(open_count, close_count, cur):
            if open_count > n: return []
            if open_count == n and close_count == n:
                self.res.append("".join(cur[::]))
                return 

            cur.append("(")
            generate(open_count+1, close_count, cur)
            cur.pop()

            if open_count > close_count:
                cur.append(")")
                generate(open_count, close_count+1, cur)
                cur.pop()

        generate(0, 0, [])
        return self.res
