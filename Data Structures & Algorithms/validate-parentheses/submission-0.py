class Solution:
    def isValid(self, s: str) -> bool:
        #open  = push to stack
        #close = check and pop

        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in closeToOpen: #check is it close bracket
                if stack and stack[-1] == closeToOpen[c]: #check top stack
                    stack.pop()
                else:
                    return False #invalid pair
            else:
                stack.append(c) #push bcs its open bracket
        
        #return true if stack is empty
        return True if not stack else False
        