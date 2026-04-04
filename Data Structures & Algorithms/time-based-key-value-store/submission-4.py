class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        li = self.data.get(key, [])

        if not li:
            return ""

        low = 0
        high = len(li) - 1

        ans = ""

        while low <= high:
            mid = (low + high) // 2
            if li[mid][0] == timestamp:
                return li[mid][1]
            elif li[mid][0] < timestamp:
                ans = li[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return ans                 