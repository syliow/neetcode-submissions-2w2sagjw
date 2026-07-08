class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # pattern: start from smallest
        numSet = set(nums)
        res = 0
        #edge case
        if len(nums) == 0:
            return 0

        for num in numSet:
            if num - 1 not in numSet:
                # found smallest
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res