class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();
        int ans = 0;
        while(low <= high){
            int mid = (low + high) / 2;
            if(isFeasible(mid, piles, h)){
                ans = mid;
                high = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean isFeasible(int candidate, int[] piles, int h){
        int res = 0;
        for(int pile: piles){
            if(pile % candidate == 0){
                res += pile /candidate;
            }else{
                res += (pile/candidate + 1);
            }
        }
        return res <= h ? true : false; 
    }
}
