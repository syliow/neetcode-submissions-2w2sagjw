class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #pattern: shortest path from a to b, k stop -> bellman ford
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices.copy()

            for u, v, w in flights:
                #havent process
                if prices[u] == float("inf"):
                    continue
                #relax edge
                if prices[u] + w < tmp[v]:
                    #update price
                    tmp[v] = prices[u] + w
            prices = tmp
        
        #if prices = inf means not reachable, return -1
        return -1 if prices[dst] == float("inf") else prices[dst]