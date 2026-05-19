class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most freq => top X element
        #count
        n_map = {} # num: count
        res = []
        for i in range(len(nums)):
            n_map[nums[i]] = 1 + n_map.get(nums[i], 0)
        
        arr = []
        for key, count in n_map.items():
            #may return in any order
            arr.append([count, key]) #sort by highest count
        #sort it 
        arr.sort()

        #return top k values
        #pop remove last ele
        while len(res) < k:
            res.append(arr.pop()[1]) #return only key
        
        return res

        
        