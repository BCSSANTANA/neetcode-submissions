class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x) + int(y))
            elif t == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x) - int(y))
            elif t == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x) * int(y))
            elif t == "/":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(int(x) / int(y)))
            else:
                stack.append(t)
        print(6 // -132)
        return int(stack[-1])