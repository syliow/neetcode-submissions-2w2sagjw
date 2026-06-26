class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            #if stuck at 0
            if farthest == i:
                return False
            if i == curEnd:
                curEnd = farthest
        return True