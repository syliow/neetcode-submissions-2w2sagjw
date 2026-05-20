class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create 2 map: one is s1 count, one is s2 count
        # always compare s2 current window (s2map vs s1map)
        # otherwise invalid window, l + 1
        # early return
        if len(s1) > len(s2):
            return False

        # Core idea: fixed sliding window
        s1map, s2map = {}, {}
        # initialization
        for i in range(len(s1)):
            s1map[s1[i]] = 1 + s1map.get(s1[i], 0)
            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
        need = len(s1map)

        # in python we can directly compare map
        if s1map == s2map:
            return True

        # if not equal, sliding window
        # slowly expand through r
        l = 0
        for r in range(len(s1), len(s2)):
            # if vaid, continue expand
            s2map[s2[r]] = 1 + s2map.get(s2[r], 0)

            # Fixed window, make sure we keep s1 length
            s2map[s2[l]] -= 1
            # if < 0 , remove
            if s2map.get(s2[l]) == 0:
                del s2map[s2[l]]
            l += 1  # move L forward

            # final comparison
            if s1map == s2map:
                return True
        return False
