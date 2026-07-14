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
            ans = ""
            for val in self.timemap[key]:
                if val[0] == timestamp:
                    return val[1]
                elif val[0] < timestamp:
                    ans = val[1]
                
            return ans
        
