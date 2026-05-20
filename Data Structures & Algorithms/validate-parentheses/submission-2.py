class Solution:
    def isValid(self, s: str) -> bool:
        strMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        #idea: check chara
        #if close , we pop
        #if open, we push
        #final stack must be empty
        for c in s:
            if c in strMap:
                #if top stack matches the pair with c
                if stack and stack[-1] == strMap[c]:
                    stack.pop()
                else:
                    #edge case: ]
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else: 
            return False