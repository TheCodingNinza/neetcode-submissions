class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[high] and target <= nums[high] and target > nums[mid]:
                low = mid + 1
            elif nums[mid] < nums[high] and target > nums[high]:
                high = mid - 1    
            elif nums[mid] < nums[high] and target < nums[mid]:
                high = mid - 1
            elif nums[low] < nums[mid] and target > nums[mid]:
                low = mid + 1
            elif nums[low] < nums[mid] and target >= nums[low] and target < nums[mid]: 
                high = mid - 1
            elif nums[low] < nums[mid] and target < nums[low]:
                low = mid + 1    
            elif nums[low] == nums[mid]:
                low = mid + 1
            elif nums[mid] == nums[high]:
                high = mid - 1        

        return -1                        