class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            # count the value for each num
            count[num] = 1 + count.get(num, 0)

        arr = []
        # do a for loop to put in count, num in res arr
        #.items returns both key and value
        for num, cnt in count.items():
            arr.append([cnt, num])
        #then sort the arr based on count (dsc order)
        arr.sort()

        #pop until we have top k remaining
        res = []
        while len(res) < k :
            #remove the last element with highest count
            last_pair = arr.pop()

            #[0] = count, [1] = num
            actual_num = last_pair[1]

            #push the num to res
            res.append(actual_num)

        return res


        