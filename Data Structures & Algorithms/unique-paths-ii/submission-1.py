class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #pattern: btm up
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)] #dp[r][c]
        #base case
        if obstacleGrid[ROWS - 1][COLS - 1] == 0:
            dp[ROWS - 1][COLS - 1] = 1 #

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                #1 is obstacle
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    #grid pos == 0
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]