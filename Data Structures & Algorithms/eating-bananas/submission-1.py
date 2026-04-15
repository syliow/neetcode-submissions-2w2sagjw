class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      #find the max num from piles
      l, r = 1, max(piles)
      res = r #the max is always a valid ans

      while l <= r:
        mid = (l + r) // 2

        #calculate time to eat
        totalTime = 0
        for p in piles:
            #round up the time to eat each pile
            totalTime += math.ceil(float(p) / mid)  
            #we found a valid ans, but might not be smallest
        if totalTime <= h:
                #record ans first
                #go left to try and find smaller valid val
                res = mid
                r = mid - 1
        else:
                l = mid + 1
      return res