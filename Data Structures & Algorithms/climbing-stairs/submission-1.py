class Solution:
    def climbStairs(self, n: int) -> int:
        # start from last to front
        # n is top , so only 1 way to reach it
        # n - 1 is one step before top, only can + 1 to reach top
        one, two = 1, 1

        # keep compare one and two for index i
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one
