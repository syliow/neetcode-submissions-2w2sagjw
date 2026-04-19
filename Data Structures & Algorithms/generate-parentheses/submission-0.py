class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add ( if open < n
        #add ) if close < open
        #complete if open == close == n
        stack = []
        res = []

        def backtrack(openN, closeN):
            #complete pair, push to res
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n: #add (
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN: #add )
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

