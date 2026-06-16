class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern: 2 pointers
        newStr = ""
        for chara in s:
            if chara.isalnum():
                newStr += chara.lower()

        l, r = 0, len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            # otherwise continue check and move inwards
            l += 1
            r -= 1
        return True  # finally only return true
