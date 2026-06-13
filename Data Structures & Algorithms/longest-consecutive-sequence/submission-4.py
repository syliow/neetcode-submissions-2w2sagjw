class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # instead of lookup 1 by 1, we start from smallest
        longest = 0
        for num in nums:
            curr = 1
            # start from smallest
            if num - 1 not in nums:
                while num + curr in nums:
                    curr += 1  # go up 1 for every check
            # compare both num
            longest = max(longest, curr)
        return longest
