class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #idea: curr tmp > top stack, pop top stack

        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                #calculate day diff
                res[stackIndx] = i - stackIndx
            stack.append((t, i))
        
        return res