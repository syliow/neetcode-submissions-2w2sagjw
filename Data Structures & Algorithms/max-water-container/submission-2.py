class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = w * h
        # we get lower height, bcs thats the max limit
        # track max, compare against current

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            # w = width, h = height
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h
            maxArea = max(maxArea, area)

            # move whichever is smaller to find the next max area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
