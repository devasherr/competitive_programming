class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif n == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(n))
        return stack[-1]