class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pair = []

        # base case
        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(pair))
                return

            if openN < n:
                pair.append("(")
                dfs(openN + 1, closeN)
                pair.pop()

            if closeN < openN:
                pair.append(")")
                dfs(openN, closeN + 1)
                pair.pop()

        dfs(0, 0)
        return res
