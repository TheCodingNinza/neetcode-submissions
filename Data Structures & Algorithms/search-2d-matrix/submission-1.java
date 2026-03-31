class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int low = 0;
        int high = m * n - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            int xCoor = mid / n;
            int yCoor = mid % n;
            // System.out.println("low: "+low);
            // System.out.println("high: "+high);
            if(matrix[xCoor][yCoor] == target)
                return true;
            else if(target > matrix[xCoor][yCoor]){
                low = mid + 1;
            }else{
                high = mid - 1;
            }    
        }
        return false;
    }
}
