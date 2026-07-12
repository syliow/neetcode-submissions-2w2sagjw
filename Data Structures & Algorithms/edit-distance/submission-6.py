class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            # base case: word1 is exhausted, return remaining length of word2
            if i == len(word1):
                return len(word2) - j
            # base case: word2 is exhausted, return remaining length of word1
            if j == len(word2):
                return len(word1) - i
            # memo check
            if (i, j) in dp:
                return dp[(i, j)]
            # recursion
            res = 0
            # if equal, just move on
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            dp[(i, j)] = res
            return res

        return dfs(0, 0)