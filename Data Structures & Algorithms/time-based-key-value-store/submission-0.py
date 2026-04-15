class TimeMap:

    def __init__(self):
        self.keyStore = {} #[val, timstamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        #do a bs
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                #we found possible ans but maybe can go closer
                res = values[mid][0] #[val, timestamp] , we want to return val
                l = mid + 1
            else:
                r = mid - 1
        return res
