class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #core idea: start from num smallest without -1 in set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                #start from the num
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

