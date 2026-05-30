class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [
            # make a row of zeros for out of bounds
            [0 for j in range(len(text2) + 1)]
            for i in range(len(text1) + 1)
        ]
        # pattern: btm up (R -> L)
        # nested for loop
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # check if chara match
                if text1[i] == text2[j]:
                    # diagonal down right
                    # formula: 1 + (Right val+ Down val)
                    # update grid
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # right neighbor and down neighbor
                    # formula: max(Right val, down val)
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # row 0, col 0 = top left corner
        return dp[0][0]
