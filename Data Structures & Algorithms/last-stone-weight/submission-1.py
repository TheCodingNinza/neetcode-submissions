class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            second_stone = -heapq.heappop(heap)
            
            
            new_stone = abs(first_stone - second_stone)
            heapq.heappush(heap, -new_stone)

        return -heapq.heappop(heap)
        