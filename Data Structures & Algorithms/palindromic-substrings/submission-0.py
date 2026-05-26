class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd
            res += self.countPalindrome(s, i, i)
            # even
            res += self.countPalindrome(s, i, i + 1)
        return res

    def countPalindrome(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count
