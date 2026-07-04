class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for bracket in s:
            # idea: pop if close bracket, push if open
            if bracket in bracketMap:
                if stack and stack[-1] == bracketMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                # open
                stack.append(bracket)

        return True if len(stack) == 0 else False
