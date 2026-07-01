class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip dup
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                # skip dup
                # j = i + 1 is the first valid second choice
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fourSum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # continue search
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif fourSum < target:
                        l += 1
                    elif fourSum > target:
                        r -= 1
        return res