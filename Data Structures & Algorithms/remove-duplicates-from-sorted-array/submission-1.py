class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #pattern: 2 pointer, arr already sorted
        #find dup
        n = len(nums)
        l, r = 0, 0
        while r < n:
            nums[l] = nums[r]
            #skip dup
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1
        return l