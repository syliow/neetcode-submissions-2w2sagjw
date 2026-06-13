class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pattern: stack. why stack? push push pop
        stack = []
        operators = {"+", "-", "/", "*"}
        for t in tokens:
            if t in operators:
                if t == "+":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int1 + int2)
                elif t == "-":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int2 - int1)
                elif t == "*":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int1 * int2)
                elif t == "/":
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(math.trunc(int2 / int1))
            else:
                stack.append(int(t))
        return stack[-1]
