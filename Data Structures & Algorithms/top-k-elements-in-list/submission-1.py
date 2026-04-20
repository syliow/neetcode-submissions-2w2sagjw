class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #{2: 50, 3: 1}
        for num, cnt in count.items(): #items is key: val
            arr.append([cnt, num])
        #sort and pop
        arr.sort() 
        while len(res) < k:
            #pop and add it to res
            prev = arr.pop()
            res.append(prev[1]) #0: cnt, 1: num
        
        return res
