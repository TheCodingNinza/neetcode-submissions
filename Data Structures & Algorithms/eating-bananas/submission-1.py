class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high + 1
        while low <= high:
            mid = (low + high) // 2
            if self.canEat(mid, piles, h):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans        




    def canEat(self, speed: int, piles: List[int], h: int) -> bool:
        timeTaken = 0;
        for pile in piles:
            if pile % speed == 0:
                timeTaken += (pile // speed)
            else:
                timeTaken += ((pile // speed) + 1)        
        
        if timeTaken <= h:
            return True
        else:
            return False    