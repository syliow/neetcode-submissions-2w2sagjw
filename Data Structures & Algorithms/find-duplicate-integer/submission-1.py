class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #cycle detection : tortoise and hare
        # loop 1 -> prove a cycle exists
        # loop 2 -> find entrance of cycle (lands on dup )
        #dummy ? no
        slow, fast = 0, 0 #both starts at 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True: #dun forget slow2 starts at 0
            slow = nums[slow]
            slow2 = nums[slow2]
            #if they meet = cycle
            if slow == slow2:
                return slow
            