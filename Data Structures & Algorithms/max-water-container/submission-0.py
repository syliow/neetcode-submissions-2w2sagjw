class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #core idea: 2 pointers, move either l or r inward for smaller val
        l, r = 0, len(heights) - 1
        res = 0

        while (l < r):
            #area = height * width
            area = min(heights[l], heights[r]) * (r-l)
            #compare area against res
            res = max(res, area)

            #move whichever is smaller
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
