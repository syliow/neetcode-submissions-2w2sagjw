class TimeMap:
    def __init__(self):
        self.keyMap = {}  # key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
        self.keyMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""

        # binary search
        res = self.keyMap[key]
        l, r = 0, len(res) - 1
        val = ""

        while l <= r:
            mid = (l + r) // 2
            if res[mid][1] == timestamp:
                return res[mid][0]  # value
            elif res[mid][1] < timestamp:
                val = res[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return val
