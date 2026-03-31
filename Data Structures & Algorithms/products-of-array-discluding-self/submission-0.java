class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int res = 1;
        int numOfZeros = 0;
        for(int num: nums){
            if(num == 0)
                numOfZeros++;
            else
                res *= num;    
        }
            
        if(numOfZeros == 0){
            for(int i=0; i < nums.length; i++){
                ans[i] = res/nums[i];
            }
        }else if(numOfZeros == 1){
            for(int i=0; i < nums.length; i++){
                if(nums[i] != 0)
                    ans[i] = 0;
                else
                    ans[i] = res;    
            }
        }else{
            for(int i=0; i < nums.length; i++){
                ans[i] = 0;    
            }
        }
        return ans;    
    }
}  
