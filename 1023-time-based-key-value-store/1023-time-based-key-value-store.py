class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = []
            
        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key].append([ timestamp, value ])
        

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""
        
        if timestamp < self.key_time_map[key][0][0]:
            return ""
        
        left = 0
        right = len(self.key_time_map[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.key_time_map[key][right - 1][1]

class TimeMap2:

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