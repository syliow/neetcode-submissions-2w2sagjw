class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # pattern: backtracking
        ROWS, COLS = len(board), len(board[0])

        def backtracking(i, r, c):
            # reach end of word = found pair
            if i == len(word):
                return True
            # base case
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or board[r][c] == "#"
                or board[r][c] != word[i]
            ):
                return False
            # add to pair, check if match with word
            # if not, undo and continue
            temp = board[r][c]
            board[r][c] = "#"

            # go thru 4 directions
            res = (
                backtracking(i + 1, r, c + 1)
                or backtracking(i + 1, r, c - 1)
                or backtracking(i + 1, r + 1, c)
                or backtracking(i + 1, r - 1, c)
            )
            board[r][c] = temp
            return res

        # run through whole grid
        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(0, r, c):
                    return True
        return False
