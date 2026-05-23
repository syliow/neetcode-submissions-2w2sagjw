class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # openN = (  => can only add openN IF openN < n
        # closeN = ) => can only add closeN IF closeN < openN
        openN, closeN = 0, 0
        res = []
        stack = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # follow core idea: do -> recursion -> undo
            # openN
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            # closeN
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(openN, closeN)
        return res
