class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        #L = unique num index
        for r in range(1, len(nums)):
            #check for dup, skip dup
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l