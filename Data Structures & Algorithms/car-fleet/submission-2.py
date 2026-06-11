class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pattern: monotonic stack (decreasing)
        # top stack is absolute
        # any car behind top stack with faster speed = merge
        # any car behind top stack slower speed = own stack
        stack = []
        cars = [[p, s] for p, s in zip(position, speed)]
        # sort based on pos, we want the car closer to target first
        cars.sort(reverse=True)

        for pos, spd in cars:
            # calculate each time to reach target for each car
            time = (target - pos) / spd
            if not stack or time > stack[-1]:  # only push to stack if its slower
                stack.append(time)

        return len(stack)
