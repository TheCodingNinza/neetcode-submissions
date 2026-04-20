class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-x for x in nums]
        heapq.heapify(self.heap)
        print(f"heap: {self.heap}")
        self.k = k

    def add(self, val: int) -> int:
        print(f"heap: {self.heap}")
        heapq.heappush(self.heap, -val)
        top_elems = []
        for i in range(self.k):
            top_elems.append(heapq.heappop(self.heap))
        required_value = top_elems[-1]
        for i in range(len(top_elems)):
            heapq.heappush(self.heap, top_elems[i])
        return -required_value    


