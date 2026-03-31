class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while(low <= high){
            int mid = (low + high) / 2;
            System.out.println("low: "+low);
            System.out.println("high: "+high);
            System.out.println("mid: "+mid);
            if(nums[mid] == target){
                return mid;
            }else if(nums[low] < nums[mid] && target < nums[mid] && target >= nums[low]){
                high = mid - 1;
            }else if(nums[low] < nums[mid] && !(target < nums[mid] && target >= nums[low])){
                low = mid + 1;
            }else if(nums[mid] < nums[high] && target > nums[mid] && target <= nums[high]){
                low = mid + 1; 
            }else if(nums[mid] < nums[high] && !(target > nums[mid] && target <= nums[high])){
                high = mid - 1;
            }else{
                // System.out.println("I m here");
                low = mid + 1;
            }
        }
        return -1;
    }
}
