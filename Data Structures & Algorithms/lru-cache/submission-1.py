class LRUCache:

    def __init__(self, capacity: int):
        
        self.keyValueMap = {}
        self.timestampKeyMap = {}
        self.min_heap = []
        self.time = 0
        self.capacity = capacity
        self.currentCapacity = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.keyValueMap:
            (value, timestamp) = self.keyValueMap[key]
            self.keyValueMap[key] = (value, self.time)
            del self.timestampKeyMap[timestamp]
            self.timestampKeyMap[self.time] = key
            heapq.heappush(self.min_heap, self.time)
            return value
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.keyValueMap:
            (oldValue, timestamp) = self.keyValueMap[key]
            self.keyValueMap[key] = (value, self.time)
            del self.timestampKeyMap[timestamp]
            self.timestampKeyMap[self.time] = key
            heapq.heappush(self.min_heap, self.time)
        else:
            if self.currentCapacity < self.capacity:
                self.currentCapacity += 1
                self.keyValueMap[key] = (value, self.time)
                heapq.heappush(self.min_heap, self.time)
                self.timestampKeyMap[self.time] = key
            else:
                min_time = heapq.heappop(self.min_heap)
                while min_time not in self.timestampKeyMap:
                    min_time = heapq.heappop(self.min_heap)
                key_to_delete = self.timestampKeyMap[min_time]
                del self.timestampKeyMap[min_time]
                del self.keyValueMap[key_to_delete]
                self.keyValueMap[key] = (value, self.time)
                self.timestampKeyMap[self.time] = key
                heapq.heappush(self.min_heap, self.time)



