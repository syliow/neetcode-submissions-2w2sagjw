class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # early return
        if len(digits) == 0:
            return []

        res, pair = [], []
        digitCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            # base case
            if i >= len(digits):
                res.append("".join(pair))
                return

            for n in digitCharMap[digits[i]]:
                pair.append(n)
                backtrack(i + 1)
                pair.pop()

        backtrack(0)
        return res
