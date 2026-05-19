class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # idea: if board piece is ".", ignore
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # 3 * 3 inside each small grid

        # nested for loop = board[r][c]

        for r in range(9):
            for c in range(9):
                # ignore .
                if board[r][c] == ".":
                    continue
                # check for invalid cases
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
            
                #if not in set, add to it
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True