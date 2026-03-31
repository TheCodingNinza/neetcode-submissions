class Solution {
    public int maxProfit(int[] prices) {
       if(prices.length == 1)
            return 0; 
       int leftPointer = 0;
       int rightPointer = 1;
       int mostProfit = 0;
       while(rightPointer < prices.length){
            int profit = prices[rightPointer] - prices[leftPointer];
            if(profit <= 0){
                leftPointer = rightPointer;
            }
            mostProfit = Math.max(mostProfit, profit);
            rightPointer++;
       }
       return mostProfit; 
    }
}
