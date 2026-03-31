class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        pred_mul_arr = []
        succ_mul_arr = []
        ans = []
        for i in range(len(nums)):
            if i != 0:
                pred_mul_arr.append(pred_mul_arr[i-1] * nums[i])
            else:
                pred_mul_arr.append(nums[i])
            succ_mul_arr.append(0)
            ans.append(0)    


        for i in range(len(nums) - 1, -1, -1):             
            if i != len(nums) - 1:
                succ_mul_arr[i] = succ_mul_arr[i+1] * nums[i]
            else:
                succ_mul_arr[i] = nums[i]

        print(pred_mul_arr)
        print(succ_mul_arr)

        for i in range(len(nums)):
            if i == 0:
                ans[i] = succ_mul_arr[i+1]
            elif i == len(nums) - 1:
                ans[i] = pred_mul_arr[i-1]
            else:
                ans[i] =  pred_mul_arr[i-1] * succ_mul_arr[i+1]  

        return ans     