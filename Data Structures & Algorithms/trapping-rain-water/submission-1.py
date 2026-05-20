class Solution:
    def trap(self, height: List[int]) -> int:
        #pattern: L R pointer
        #move which every pointer has smaller value

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                #move L bcs L is smaller
                l += 1
                #update leftmax again
                leftMax = max(leftMax, height[l])
                #count the trapped block of water
                res += leftMax - height[l]
            else:
                #if R is smaller
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        