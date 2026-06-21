class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        pair = []
        # early return
        if len(digits) == 0:
            return []

        def dfs(i):
            # base case
            if i >= len(digits):
                res.append("".join(pair))
                return

            for digit in digitsMap[digits[i]]:
                pair.append(digit)
                dfs(i + 1)

                pair.pop()

        dfs(0)
        return res
