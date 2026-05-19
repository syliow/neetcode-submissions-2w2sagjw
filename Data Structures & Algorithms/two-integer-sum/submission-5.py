class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea: use target to - nums[i] until we found answer
        num_map = {}  # value: index

        for i in range(len(nums)):
            two_sum = target - nums[i]
            if two_sum in num_map:
                return [num_map.get(two_sum), i]

            num_map[nums[i]] = i
