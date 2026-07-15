class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        print(numCount)
        for key, count in numCount.items():
            if count > len(nums) // 2:
                return key
