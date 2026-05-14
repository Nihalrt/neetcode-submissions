from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        else:
            array = self.store[key]
            l = 0
            r = len(array) - 1
            mid = 0
            while l<=r:
                mid = (l+r) // 2
                if array[mid][1] == timestamp:
                    return array[mid][0]
                elif timestamp < array[mid][1]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return array[r][0] if r >= 0 else ""

            
        
