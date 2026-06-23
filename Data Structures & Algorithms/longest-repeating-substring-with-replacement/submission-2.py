class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charaMap = {}
        longest = 0
        maxFreq = 0
        for r in range(len(s)):
            charaMap[s[r]] = charaMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, charaMap.get(s[r]))
            # invalid conditions: cur win len > k
            while ((r - l + 1) - maxFreq) > k:
                charaMap[s[l]] = charaMap.get(s[l]) - 1
                l += 1
            # compare max vs cur
            longest = max(longest, r - l + 1)
        return longest
