class Solution {
    public int longestConsecutive(int[] nums) {
        int ans = 0;
        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        for(int num: nums){
            if(!numSet.contains(num-1)){
                int tempAns = 1;
                int nextInteger = num + 1;
                while(numSet.contains(nextInteger)){
                    tempAns++;
                    nextInteger++;
                }   
                ans = Math.max(tempAns, ans);    
            }
        }
        return ans;
    }
}
