class Solution:
    def isValid(self, s: str) -> bool:
        #pattern: stack, if matches pair we pop
        stack = []
        bracket = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for chara in s:
            #close bracket
            if chara in bracket:
                #check whether they match or not
                if stack and stack[-1] == bracket[chara]:
                    stack.pop()
                else:
                    return False #invalid pair
            else:
                stack.append(chara) #push to stack if its open
        return True if not stack else False