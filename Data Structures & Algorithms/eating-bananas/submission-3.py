class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pattern: binary search (bcs we need to look thru min -> max in arr)
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2  # potential eating speed
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            # maybe found possible ans, but go further
            if hours <= h:
                res = mid
                # [1, 2, 3(mid), 4, 5]
                r = mid - 1
            else:
                l = mid + 1
        return res
