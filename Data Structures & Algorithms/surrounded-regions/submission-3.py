class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # directly modify board so dunnid track visited
        # pattern: DFS, start from border cell, inwards dfs

        # core idea: flip border cell to T
        # change connected O -> X
        # flip back T -> O

        def dfs(r, c):
            # base case: invalid case
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # check for top, btm borders
        for r in range(ROWS):
            # top row
            if board[r][0] == "O":
                dfs(r, 0)
            # btm row
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # Check for left, right col
        for c in range(COLS):
            # left col
            if board[0][c] == "O":
                dfs(0, c)
            # right col (last col)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        # go thru every single grid, flip connecteds o -> X
        # flip T back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"
