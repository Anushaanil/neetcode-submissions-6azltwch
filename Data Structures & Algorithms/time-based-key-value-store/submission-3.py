class TimeMap:
    # Bruteforce
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.timemap:
        #     self.timemap[key] = [[timestamp, value]]
        # else:
        #     self.timemap[key].append([timestamp, value])
        self.timemap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
            
        values = self.timemap[key]
        left, right = 0, len(values) - 1
        ans = ""

        while left <= right:
            mid = (left+right)//2
            mid_timestamp, mid_val = values[mid]

            if mid_timestamp == timestamp:
                return mid_val
            elif mid_timestamp < timestamp:
                ans = mid_val
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
            