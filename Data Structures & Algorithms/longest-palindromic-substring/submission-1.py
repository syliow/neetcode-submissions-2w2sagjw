class Solution:
    def longestPalindrome(self, s: str) -> str:
        # pattern: 2 pointers
        # instead of most L and most R, we pick one char index and exand outwards
        # issue: how to find the middle of palindrome
        res = ""
        for i in range(len(s)):
            # odd length
            odd = self.expand(s, i, i)
            # even length
            even = self.expand(s, i, i + 1)
            # compare length of both odd and even with res
            if len(odd) > len(even):
                currLongest = odd
            else:
                currLongest = even

            if len(currLongest) > len(res):
                res = currLongest

        return res

    def expand(self, s, l, r):
        # abb: start from b (L, R same) -> ODD
        # abba: start from bb (L = b, r = b) -> EVEN
        # as long both match and within bounds, keep expanding
        while (l >= 0 and r < len(s)) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]
