class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach (space optimized)
        prev1, prev2 = 0, 0

        for i in reversed(range(len(nums))):
            # either rob current or skip current and rob 2 house after
            # <---- cur prev1 prev2
            cur = max(prev1, nums[i] + prev2)
            prev1, prev2 = cur, prev1

        return prev1
