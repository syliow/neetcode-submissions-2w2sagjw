class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # pattern: 2d dp -> track index from word1 and word2
        dp = {}  # [(i, j)]

        def dfs(i, j):
            # base case: word1 reach end index, but not word2
            # eg: word1 = "" word2 = "cat", 3 operations (insert)
            # add -j bcs j maybe moved already
            if i >= len(word1):
                return len(word2) - j

            # base case: word2 reach end index
            if j >= len(word2):
                return len(word1) - i

            # base case: both pointers pointing to same chara
            if word1[i] == word2[j]:
                # return 0 <- wrong bcs stop recursion
                return dfs(i + 1, j + 1)  # move forward w/o cost

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion: find min operations
            res = 0
            res = min(
                # each operation should + 1
                1 + dfs(i + 1, j),  # del chara
                1 + dfs(i, j + 1),  # insert chara
                1 + dfs(i + 1, j + 1),  # replace chara
            )
            dp[(i, j)] = res
            return res

        return dfs(0, 0)  # both word start from index 0
