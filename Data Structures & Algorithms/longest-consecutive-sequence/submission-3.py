class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(n) time = cannot sort
        # start from smallest, num without -1 in set
        num_set = set(nums)  # avoid dup
        longest = 0

        for n in num_set:
            length = 0
            # start from smallest
            if n - 1 not in num_set:
                length = 1  # default is 1

                while n + 1 in num_set:
                    length += 1
                    # move pointer forward
                    n += 1
                # check for every num
                longest = max(longest, length)

        return longest
