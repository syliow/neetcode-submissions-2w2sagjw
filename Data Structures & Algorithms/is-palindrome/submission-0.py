class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        #loop through each chara in s and add to new str
        for c in s:
            #check for alphanumeric
            if c.isalnum():
                newStr += c.lower()
        #check for palindrome
        #from first chara to last chara, go backwards (::-1)
        return newStr == newStr[::-1]

        