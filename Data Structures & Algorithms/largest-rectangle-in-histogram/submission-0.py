class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights):
            start = i

            #if the bar we found (h) < top of stack, bar cant stretch further to right
            #so we need to pop it
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) #area
                start = index #short bar can start at tall bar index
            stack.append((start, h)) #push curr bar back to stack

            #clean up for remaining bars
            #stretch from start index all the way to end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea