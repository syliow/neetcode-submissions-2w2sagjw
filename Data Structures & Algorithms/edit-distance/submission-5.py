class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}  # [i, j]

        # make word1 == word2
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            # base case: run out of options
            if i == len(word1):
                return len(word2) - j
            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            res = 0
            # if both chara match
            # no cost, move pointer forward without cost
            if word1[i] == word2[j]:
                res += dfs(i + 1, j + 1)
            else:
                # find min operations
                res += 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
