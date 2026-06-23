class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pattern: sliding + set
        visited = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            # if invalid window, move l forward
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            maxLength = max(maxLength, r - l + 1)  # compare max vs cur window len
        return maxLength
