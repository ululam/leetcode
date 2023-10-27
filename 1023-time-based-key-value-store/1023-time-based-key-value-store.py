class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        lst = self.map[key]
        return self._binary_search(lst, timestamp)

    def _binary_search(self, lst, timestamp):
        left, right = 0, len(lst)-1
        t, val = 0, ""
        while left <= right:
            mid = left + ((right - left) >> 1)
            t, val = lst[mid]
            if t == timestamp:
                return val
            if t < timestamp:
                if mid < len(lst)-1 and lst[mid+1][0] > timestamp:
                    return val
                left = mid + 1
            else:
                right = mid - 1
        return val if t <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)