class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # pattern: bellman ford
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            # copy arr for iterations
            tmpPrices = prices.copy()

            # process all edge
            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                # check price
                if prices[source] + price < tmpPrices[destination]:
                    tmpPrices[destination] = prices[source] + price
            # update price
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1