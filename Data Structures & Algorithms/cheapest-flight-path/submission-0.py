class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s = source, d = destination, p= price
                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            # update price after K iteration
            prices = tmpPrices
        # if prices = infinity means not reachable, return -1
        return -1 if prices[dst] == float("inf") else prices[dst]
