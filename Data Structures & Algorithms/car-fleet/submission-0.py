class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #reverse it and compare against top stack

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True) #sort by pos (dsc)
        stack = []

        for p, s in pair: #reverse sorted order
            time = (target - p) / s #time = (target - pos) / speed
            stack.append(time)

            #compare curr car time against top stack
            #stack must at least have 2 fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) #remaining item in stack = fleet