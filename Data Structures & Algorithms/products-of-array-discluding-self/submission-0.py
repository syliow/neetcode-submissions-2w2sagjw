class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # define 3 arr
        n = len(nums)

        preffix = [0] * n
        suffix = [0] * n
        res = [0] * n

        #pref most left = 1, suff most right = 1
        preffix[0] = suffix[n - 1] = 1
        
        #pref (start from left)
        for i in range(1, n):
            preffix[i] = nums[i - 1] * preffix[i - 1]
        
        #suf (start from right) <- reverse for loop
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        #multiply suff and pref
        for i in range(n):
            res[i] = preffix[i] * suffix[i]
        
        return res