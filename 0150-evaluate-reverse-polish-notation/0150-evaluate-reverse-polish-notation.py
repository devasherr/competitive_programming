class Solution:
    def evalRPN(self, tokens) -> int:
        stack = [] 

        for t in tokens:
           if t == "+":
               stack.append(stack.pop() + stack.pop())
           elif t == "*":
               stack.append(stack.pop() * stack.pop())
           elif t == "-":
               n1 = stack.pop()
               n2 = stack.pop()
               stack.append(n2 - n1)
           elif t == "/":
               n1 = stack.pop()
               n2 = stack.pop()
               stack.append(int(n2 / n1))
           else:
               stack.append(int(t))

        return stack[0]
