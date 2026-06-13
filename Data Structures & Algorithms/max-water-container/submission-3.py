class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # pattern: 2 pointers
        # idea: keep max h bar, move bar with lower h inwards
        l, r = 0, len(heights) - 1
        maxWater = 0
        # not finding a target, and l r cannot be at same
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            curWater = w * h
            maxWater = max(maxWater, curWater)

            if heights[l] < heights[r]:
                l += 1  # l smaller
            else:
                r -= 1  # r smaller

        return maxWater
