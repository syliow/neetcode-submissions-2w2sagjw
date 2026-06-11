class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern: 1d dp, why? bcs we just need index
        # subproblem: do we include the next number in current subsequence? or skip it
        # btm up L-> R
        n = len(nums)
        # base case:all chara at least has 1 subsequence
        dp = [1] * n
        
        # R -> L (start at 2nd last index)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # i move towards L
                # j move towards R
                if nums[i] < nums[j]:
                    # consider extend
                    # dp[j] + 1 = neighbor pair + cur
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp) #longest substr can start from any index