class TimeMap:
    def __init__(self):
        self.timemap = {}  # key: [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timemap.get(key, [])
        l, r = 0, len(values) - 1

        if key in self.timemap:
            # since time is linear, we can do BS
            while l <= r:
                mid = (l + r) // 2
                if values[mid][1] <= timestamp:
                    # we found a valid ans, but might not be closest
                    res = values[mid][0]  # return value
                    l = mid + 1
                else:
                    r = mid - 1
        return res
