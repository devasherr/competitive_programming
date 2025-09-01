class TimeMap:
    def __init__(self):
        self.timestamp = defaultdict(list) # key: [time, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # didn't know timestamp was strictly increasing :(
        self.timestamp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp: return ""
        left, right = 0, len(self.timestamp[key]) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if self.timestamp[key][mid][0] <= timestamp:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        if res == -1: return ""
        return self.timestamp[key][res][1]
