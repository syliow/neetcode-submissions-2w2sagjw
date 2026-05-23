class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3 set
        col = set()
        posDiag = set()
        negDiag = set()

        # initialize a board
        board = [["."] * n for i in range(n)]
        res = []

        # focus more on row
        def backtrack(r):
            # base case: we check every row unti last row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # core idea: include, backtrack, exclude
            for c in range(n):
                # check invalid conditions
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"  # mark spot as queen

                # check next row
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
