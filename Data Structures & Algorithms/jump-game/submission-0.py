class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #idea: start from last index, move goal forward
        goal = len(nums) - 1

        for i in range(len(nums) -2 , -1, -1):
            #if nums[i] + index can reach goal, move goal pos forward
            if i + nums[i] >= goal:
                goal = i
        return goal == 0