class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):                
            # check for warmer day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevDayIdx = stack.pop()
                res[prevDayIdx] = i - prevDayIdx
            stack.append(i)  #otherwise push to stack and wait for a warmer day
        return res
