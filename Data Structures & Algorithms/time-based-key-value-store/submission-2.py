class TimeMap:
    # Bruteforce
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [[timestamp, value]]
        else:
            self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        else:
            left = 0
            right = len(self.timemap[key]) - 1
            ans = ""

            while left <= right:
                mid = (left+right)//2
                val = self.timemap[key][mid]

                if val[0] == timestamp:
                    return val[1]
                elif val[0] < timestamp:
                    ans = val[1]
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return ans
            