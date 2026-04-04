class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = 1001

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                break      
                

        return ans            
