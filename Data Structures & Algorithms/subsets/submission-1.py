class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = list()

        for i in range(0, n + 1):
            self.solve(i, nums, 0, ans, list())
        return ans


    def solve(self, sze: int, nums: List[int], pos: int, ans: List[List[int]], curr_arr: List[int]) -> None:
        
        if sze == 0:
            ans.append(curr_arr)
            return

        for i in range(pos, len(nums)):
            temp_arr = curr_arr.copy()
            temp_arr.append(nums[i])
            self.solve(sze - 1, nums, i + 1, ans, temp_arr)

                
                 




        
        