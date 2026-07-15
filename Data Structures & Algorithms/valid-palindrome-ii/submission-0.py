class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                # l == r
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # skip one chara
                return isPali(l + 1, r) or isPali(l, r - 1)
            # if both equal
            l += 1
            r -= 1
        return True
