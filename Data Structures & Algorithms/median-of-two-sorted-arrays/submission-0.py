class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute force: combine into 1 array, sort it
        len1, len2 = len(nums1), len(nums2)
        merged = nums1 + nums2
        merged.sort()
        

        totalLength = len(merged)
        if totalLength % 2 == 0: #odd num
            return (merged[totalLength // 2 - 1] + merged[totalLength // 2]) / 2.0
        else:
            return merged[totalLength // 2] #even num

