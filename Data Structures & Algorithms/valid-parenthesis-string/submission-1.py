class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            else:
                #closing )
                if not left and not star:
                    return False
                #we always pop from left first if possible
                if left:
                    left.pop()
                else:
                    star.pop()
        #continue loop as long there is 1 open bracket left
        while left and star:
            if left.pop() > star.pop():
                return False
        #if left = empty, return true, else false
        return not left