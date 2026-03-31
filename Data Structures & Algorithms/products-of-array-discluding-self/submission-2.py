class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        suffix = 1;
        ans = [1] * n

        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        prefix = 1
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]


        return ans        
