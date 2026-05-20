class MinStack:
    # pattern: stack, use 2 stack
    # one is track sequence, one is track min val seen
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push to both stack
        self.stack.append(val)
        # val < top min stack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if self.minStack[-1] == removed:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
