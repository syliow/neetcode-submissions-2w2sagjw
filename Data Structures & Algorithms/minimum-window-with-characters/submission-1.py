class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        #use 2 map to keep track chara count 
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        #condition is matched when have == need
        have, need = 0, len(countT)
        #store the pos index for string
        res, resLen = [-1, -1], float("infinity")

        #store for window map
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1

        #compare have and need
            while have == need:
                #check if current window is smaller than reslen
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                #try to shrink the window to find min window size
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        #cut out the string using chara index
        if resLen != float("infinity"):
            l, r = res
            return s[l: r+1]
        else:
            return ""