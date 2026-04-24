class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = 0
        y = 0
        res = 0
        stack = []
        for t in tokens:
            if t in "+-/*":
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    res = x + y
                    stack.append(res)
                elif t == "-":
                    res = x - y
                    stack.append(res)
                elif t == "*":
                    res = x*y
                    stack.append(res)
                elif t == "/":
                    if y == 0:
                        stack.append(0)
                    else:
                        stack.append(int(x / y))
            else:
                stack.append(int(t))
        return stack[0]





        