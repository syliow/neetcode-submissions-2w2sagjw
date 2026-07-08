class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # obstacle = 1 <- skip 1
        # only move down or right
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}  # (r, c)

        def dfs(r, c):
            # base case
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or obstacleGrid[r][c] == 1
            ):
                return 0
            # base case: reach goal (btm right)
            if r == ROWS - 1 and c == COLS - 1:
                return 1  # count as 1 path

            # memo check
            if (r, c) in dp:
                return dp[(r, c)]

            # recursion
            res = 0
            # only move down / right
            res += dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res
            return res

        return dfs(0, 0)
