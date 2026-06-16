class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = list()
        
        self.solve(nums, ans, list(), target, 0, 0)
        return ans


    def solve(self, nums: List[int], ans: List[List[int]], curr_arr: List[int], target: int, targetSum: int, pos: int) -> None:

        if target == targetSum:
            ans.append(curr_arr.copy())
            return

        if target < targetSum:
            return    

        for i in range(pos, len(nums)):
        
            curr_arr.append(nums[i])
            self.solve(nums, ans, curr_arr, target, targetSum + nums[i], i)
            curr_arr.pop()
        