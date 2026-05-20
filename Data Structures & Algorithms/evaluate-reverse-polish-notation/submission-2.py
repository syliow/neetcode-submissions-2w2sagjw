class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #idea: num num operation
        for c in tokens:
            if c == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            
            elif c == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            
            elif c == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            
            elif c == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.trunc(num2 / num1))
            
            else:
                #c is number, push it
                stack.append(int(c))
        return stack[0]