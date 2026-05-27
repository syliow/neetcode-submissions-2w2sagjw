class Solution:
    def climbStairs(self, n: int) -> int:
        #pattern: btm up (optimized)
        #instead of storing whole arr, we can just use 2 value
        one, two = 1, 1

        for i in range(n - 1):
            #backup one first before moving
            tmp = one
            one = one + two
            two = tmp

        return one