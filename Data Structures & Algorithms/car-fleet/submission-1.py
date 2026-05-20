class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pattern: monotonic stack
        # either in increasing or decreasing order
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        # sort cars by dsc order (closest to target by pos)

        for i, v in enumerate(cars):
            pos = v[0]
            spd = v[1]
            # calculate time to reach goal
            # if time <= leader (merge)
            # if time > leader (form own fleet)
            time = (target - pos) / spd

            # push to stack if stack empty or slower
            if not stack or time > stack[-1]:
                stack.append(time)
            #otherwise do nthg
  
        return len(stack)
