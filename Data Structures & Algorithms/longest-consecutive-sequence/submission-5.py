class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # instead of lookup 1 by 1, we start from smallest
        longest = 0
        numSet = set(nums)

        for num in nums:
            curr = 1
            # start from smallest
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                #compare both num
                longest = max(longest, length)
        return longest
               