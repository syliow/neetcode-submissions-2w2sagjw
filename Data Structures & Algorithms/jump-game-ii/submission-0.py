class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curEnd = 0 #end of range for cur jump
        farthest = 0 #farthest we can jump 

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            #if reach end of list
            if i == curEnd:
                jumps += 1
                curEnd = farthest
        return jumps