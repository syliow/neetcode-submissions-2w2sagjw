class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            # add to set
            numSet.add(num)
