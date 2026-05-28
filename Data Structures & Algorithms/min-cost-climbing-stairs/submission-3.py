class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: btm up approach (L -> R) Optimized
        # use 2 values instead of whole dp arr
        prev1, prev2 = 0, 0

        # L -> R, stop before cost length
        for i in range(2, len(cost) + 1):
            #previous cost to reach current step + cost to move to next step
            currentCost = min(prev1 + cost[i - 1], prev2 + cost[i - 2])

            # update var to move right
            prev2 = prev1
            prev1 = currentCost

        return prev1
