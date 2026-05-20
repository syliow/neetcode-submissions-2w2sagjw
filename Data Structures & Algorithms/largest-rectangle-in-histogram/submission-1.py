class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # index

        heights.append(0)  # added 0 to sort of break final loop
        for i, h in enumerate(heights):
            # if stack is empty push
            # if top stack h > h, we pop
            while stack and heights[stack[-1]] > h:
                poppedIndex = stack.pop()
                # calculate maxarea with prev height
                height = heights[poppedIndex]

                # Find width from stack
                if not stack:
                    width = i
                else:
                    # get from top stack
                    width = i - stack[-1] - 1

                # calculate max area
                maxArea = max(maxArea, width * height)
            # if current bar is higher, push to stack
            stack.append(i)
        return maxArea
