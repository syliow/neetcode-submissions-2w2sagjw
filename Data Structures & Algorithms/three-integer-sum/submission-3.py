class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort, use LR pointer
        nums.sort()
        res = []
        # key idea: fixed num + L + R
        for i in range(len(nums)):
            # early return
  
            l, r = i + 1, len(nums) - 1
            #i can have dup too, but dun check for first
            if i > 0 and nums[i] == nums[i -1]:
                continue

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # move pointer forward
                    l += 1
                    r -= 1
                    # no dup, compare with prev num and skip
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total < 0:
                    l += 1  # we need larger num
                else:
                    r -= 1  # we need smaller num

        return res
