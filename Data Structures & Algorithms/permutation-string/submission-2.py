class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        s2Map = {}

        if len(s1) > len(s2):
            return False
        # pattern: fixed sliding window
        for chara in s1:
            s1Map[chara] = s1Map.get(chara, 0) + 1
        l = 0
        for r in range(len(s2)):
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            if (r - l + 1) == len(s1):
                if s1Map == s2Map:
                    return True
            # invalid window = over s1.length
            if (r - l + 1) >= len(s1):
                s2Map[s2[l]] = s2Map.get(s2[l]) - 1
                if s2Map.get(s2[l]) == 0:
                    del s2Map[s2[l]]
                l += 1
        return False
