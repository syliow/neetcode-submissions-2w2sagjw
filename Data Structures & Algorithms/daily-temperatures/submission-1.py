class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # idea: top stack should always keep highest temp we seen
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # we need index, used for calculate day diff
            # if stack empty, push
            # if cur val > top stack. pop
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevDayIndex = stack.pop()
                dayDiff = i - prevDayIndex
                res[prevDayIndex] = dayDiff
            else:
                stack.append(i)

        return res
