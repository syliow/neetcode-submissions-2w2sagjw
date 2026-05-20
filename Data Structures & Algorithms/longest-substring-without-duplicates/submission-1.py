class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      #pattern: set + sliding window because no dup
      #early return
        if not s: 
            return 0  
        charaSet = set()
        maxLength = 0

        l = 0
        for r in range(len(s)):
            #chara in set = invalid window
            while s[r] in charaSet:
                #remove s[l] chara from set
                charaSet.remove(s[l])
                l += 1

            #valid window: no duplicate
            charaSet.add(s[r])
            #compare against current window
            maxLength = max(maxLength, r - l + 1)

        return maxLength
        