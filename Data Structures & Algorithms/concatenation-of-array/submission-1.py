class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #two pass
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans