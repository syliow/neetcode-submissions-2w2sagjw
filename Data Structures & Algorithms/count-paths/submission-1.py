class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # first we create a btm row
        # base case is 1
        #m = row, n = col
        btmRow = [1] * n

        for i in range(m - 1):
            # create top row on top of btm
            topRow = [1] * n
            # start from 2nd last bcs last col is always 1
            for j in range(n - 2, -1, -1):
                # assign toprow
                # formula = right + down
                topRow[j] = topRow[j + 1] + btmRow[j]
            btmRow = topRow
        return btmRow[0]
