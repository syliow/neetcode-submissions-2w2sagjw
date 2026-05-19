class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern: L R pointer
        l, r = 0, len(s) - 1
        s = s.lower()  # edge case: uppercase letters

        while l < r:
            # is alnum = proceed
            # not alnum = skip
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # both is alnum, check equal
            if s[l] != s[r]:
                return False
            # if match , we want to keep checking
            l += 1
            r -= 1

        return True
