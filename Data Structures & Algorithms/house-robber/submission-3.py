class Solution:
    def rob(self, nums: List[int]) -> int:
        #pattern: btm up (optimized)
        #use 2 value

        rob1, rob2 = 0, 0
        #2 choice: skip current keep prev best, rob: get curr + best from 2
        for i in range(len(nums)):
            #either skip current house, or rob current + go to next 2 house
            #-2 house(rob2), -1 house(rob1) , curr(tmp) ->
            #to move forward: swap rob2 with rob1 and rob1 with tmp
            tmp = max(rob1, nums[i] + rob2)
            rob2 = rob1
            rob1 = tmp
        return rob1
