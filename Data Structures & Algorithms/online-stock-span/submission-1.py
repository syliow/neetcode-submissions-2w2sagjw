class StockSpanner:
    #less than or equal to cur price
    #compare the num in arr vs today price
    def __init__(self):
        self.stack = [] #(price, span)

    def next(self, price: int) -> int:
        span = 1 

        #monotonic stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)