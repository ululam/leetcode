class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.map[key][0][0]:
            return ""
                    
        lst = self.map[key]
        return self._binary_search(lst, timestamp)

    def _binary_search(self, lst, timestamp):
        # left, right = 0, len(lst)
        # while left < right:
        #     mid = (left + right) // 2
        #     if lst[mid][0] <= timestamp:
        #         left = mid + 1
        #     else:
        #         right = mid

        # # If iterator points to first element it means, no time <= timestamp exists.
        # return "" if right == 0 else lst[right - 1][1]        

        left, right = 0, len(lst)
        t, val = 0, ""
        while left < right:
            mid = left + ((right - left) >> 1)
            t, val = lst[mid]
            if t == timestamp:
                return val
            if t < timestamp:
                left = mid + 1
            else:
                right = mid
        return val if t <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)