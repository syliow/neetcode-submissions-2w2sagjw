class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # pattern: set
        num_set = set()

        for num in nums:
            if num in num_set:
                return True  # dup found
            # add to set
            num_set.add(num)
        return False
