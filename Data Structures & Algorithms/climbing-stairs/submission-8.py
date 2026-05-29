class Solution:
    def climbStairs(self, n: int) -> int:
        # pattern: btm up approach (space optimized)
        # use 2 values instead of whole dp arr
        prev1, prev2 = 1, 1

        # <---------------- n
        #    cur, prev1, prev2

        # start from last 2 pos, stop before 0, -1 every iteration
        for n in range(n - 2, -1, -1):
            # basically just keep on adding
            prev1, prev2 = prev1 + prev2, prev1
        return prev1
