class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        # initialize countT first
        for c in t:
            countT[c] = 1 + countT.get(c, 0)  # def is 0
        have, need = 0, len(countT)
        l = 0
        res = []  # store as index
        minLength = float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # check against both map, if match, increase have
            if c in countT and countT[c] == window[c]:
                have += 1

            # compare have vs need (while bcs we need keep loop)
            while have == need:
                # keep move L to find shortest
                if r - l + 1 < minLength:
                    res = s[l : r + 1]  # we stored index
                    minLength = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        if len(res):
            return res
        else:
            return ""
