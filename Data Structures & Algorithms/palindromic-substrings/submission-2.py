class Solution:
    def countSubstrings(self, s: str) -> int:
        # pattern: DP. Why? return num of substr
        dp = {}  # [i, j]
        res = 0

        def dfs(i, j):
            # empty str/ single chara
            if i >= j:
                return True

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion: chara match
            dp[(i, j)] = (s[i] == s[j]) and dfs(i + 1, j - 1)
            return dp[(i, j)]

        # check every possible substring
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i, j):
                    res += 1
        return res
