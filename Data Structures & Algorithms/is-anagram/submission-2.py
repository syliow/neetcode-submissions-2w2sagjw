class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check length first

        if len(s) != len(t):
            return False
        
        #map (dict)
        countS, countT = {}, {}

        for i in range(len(s)):
            # .get (key, def value)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)
        return countS == countT