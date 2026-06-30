class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # pattern: subarr + min size -> var sliding window
        l = 0
        res = float("inf")  # smallest length subarr
        curSum = 0
        for r in range(len(nums)):
            # keep move r until window is invalid
            # invalid window
            curSum += nums[r]
            # as long valid ans, shrink window as much as possible
            while curSum >= target:
                # compare against cur win length before we move
                res = min(res, r - l + 1)

                curSum -= nums[l]
                l += 1

        return res if res != float("inf") else 0
