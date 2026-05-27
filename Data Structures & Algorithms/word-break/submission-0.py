class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # base case for last index = always true
        dp[len(s)] = True

        # start from backwards, stop before 0, -1 every iteration
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # check word in dict against s string
                # if length w > len s = auto invalid
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # if its true, break
                if dp[i]:
                    break
        return dp[0]
