class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # pattern: why sliding window?
        # bcs we are going through 1 by 1 possible
        # core idea: window size - max freq <= k
        count = {}
        l = 0
        maxFreq = 0
        res = 0
        # we count maxfreq during expanding
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count.get(s[r]))

            # invalid: when window size - maxfreq not > k
            # move l forward
            while (r - l + 1 - maxFreq) > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            res = max(res, r - l + 1)  # longest substr length

        return res
