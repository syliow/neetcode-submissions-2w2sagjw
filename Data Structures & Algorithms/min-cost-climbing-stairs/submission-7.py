class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: btm up approach (space optimized)
        n = len(cost)
        prev1, prev2 = 0, 0

        for i in range(2, n + 1):
            # ---------> prev2 (1), prev1 (2) , cur (3)
            # --------->        prev2   prev1
            cur = min(cost[i - 2] + prev2, cost[i - 1] + prev1)
            prev1, prev2 = cur, prev1

        return prev1
