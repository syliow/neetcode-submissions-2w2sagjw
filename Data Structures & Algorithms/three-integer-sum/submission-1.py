class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #2 pointers
        res = []
        #we must sort the arr to avoid dup
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            #skip dup
            if i > 0 and a == nums[i-1]:
                continue
            
            #declare l and r
            l, r = i + 1, len(nums) - 1
            while (l < r):
                total = a + nums[l] + nums[r]

                #if > 0 , we want smaller num so r--,
                #if <0, we want larget num so l++
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                #found a 3sum == 0
                else:
                    res.append([a, nums[l], nums[r]])
                    #move on to next num
                    l += 1
                    r -= 1
                    #prevent dup
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

