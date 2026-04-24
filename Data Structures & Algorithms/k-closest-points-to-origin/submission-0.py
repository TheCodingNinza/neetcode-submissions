class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            dis = math.sqrt((point[0]) **2 + (point[1]) ** 2)
            heapq.heappush(distance, (dis, point))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distance)[1])

        return ans    