class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all space and only keep alphanumeric chara
        s = s.replace(" ", "")
        newStr = ""
        for chara in s:
            if chara.isalnum():
                newStr += chara.lower()

        l, r = 0, len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True
