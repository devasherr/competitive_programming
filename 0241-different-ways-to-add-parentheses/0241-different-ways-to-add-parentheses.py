class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def mergeLists(left, right, exp):
            res = []
            for n in left:
                for m in right:
                    if exp == "+":
                        res.append(n+m)
                    if exp == "*":
                        res.append(n*m)
                    if exp == "-":
                        res.append(n-m)
            return res


        def func(exp):
            if len(exp) < 3:
                return [int(exp)]
            
            res = []
            for i in range(len(exp)):
                if exp[i] in ["+", "*", "-"]:
                    left = func(exp[:i])
                    right = func(exp[i+1:])
                    res.extend(mergeLists(left, right, exp[i]))
            return res
        
        return func(expression)