class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #pattern: btm up 
        n = len(nums) 
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1 #1 is default way {i, total}

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
                
        return dp[n][target]