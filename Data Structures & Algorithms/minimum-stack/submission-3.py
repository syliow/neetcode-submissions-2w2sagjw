class MinStack:
    #pattern: we can use 2 stack
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)  

    def pop(self) -> None:
        #smallest val should always be on top
        val = self.stack.pop()
        if self.minstack[-1] == val:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
