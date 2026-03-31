class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(0, len(nums)):
            second_num = target - nums[i]
            if second_num in nums_dict:
                return  [nums_dict[second_num], i]
            else:
                nums_dict[nums[i]] = i              
            
        