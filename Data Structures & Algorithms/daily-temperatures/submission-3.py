class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # need to find a warmer day = stack, elements that wait for something
        res = [0] * len(temperatures)
        stack = []  # (index, temp)

        for i, v in enumerate(temperatures):
            # found a warmer day (higher than top stack)
            while stack and v > stack[-1][1]:
                [index, val] = stack.pop()
                dayDiff = i - index
                res[index] = dayDiff

            stack.append((i, v))

        return res
