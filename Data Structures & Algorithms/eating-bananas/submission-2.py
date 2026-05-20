class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # min is 1 banana per hour
        res = 0

        while l <= r:
            totalTime = 0

            mid = (l + r) // 2
            for p in piles:
                totalTime += math.ceil((p / mid))

            # if found a num we can slowly finish within limit
            if totalTime <= h:
                res = mid
                # valid ans but might not be smallest
                # try to eat lesser
                r = mid - 1
            else:
                l = mid + 1

        return res
