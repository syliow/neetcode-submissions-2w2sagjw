class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            # base case: if out of bounds
            if l > r:
                return 0
            # memo check
            if (l, r) in dp:
                return dp[(l, r)]

            maxCoins = 0
            # r + 1 to loop until last item
            for i in range(l, r + 1):
                # clear L and R side first, get coins earned
                coins = dfs(l, i - 1) + dfs(i + 1, r)
                # clear middle (i element)
                coins += nums[l - 1] * nums[i] * nums[r + 1]
                maxCoins = max(maxCoins, coins)
            dp[(l, r)] = maxCoins
            return maxCoins

        return dfs(1, len(nums) - 2)
