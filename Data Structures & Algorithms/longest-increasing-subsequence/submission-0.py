class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) #1 is the base case

        #btm up approach
        for i in range(len(nums) - 1, -1 , -1):
            for j in range(i + 1, len(nums)):
                #if i > j, then its not in increasing order anymore
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)