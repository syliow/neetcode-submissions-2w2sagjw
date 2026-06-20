class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # pattern: direct modify grid
        # ignore everything in Up down left right border
        # border O -> T
        # outside border O -> X
        # border T -> O
        def dfs(r, c):
            # base case
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            # look through 4 directions
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r - 1, c)
            dfs(r, c + 1)

        # border O -> T
        for row in range(ROWS):
            # L and right border
            dfs(row, 0)  # L
            dfs(row, COLS - 1)  # R

        for col in range(COLS):
            # Top and btm border
            dfs(0, col)  # top
            dfs(ROWS - 1, col)  # btm

        # Outside border O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                # Revert Temp T -> O (border)
                if board[r][c] == "T":
                    board[r][c] = "O"
