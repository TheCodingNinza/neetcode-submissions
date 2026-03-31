class Solution {
    public int[] topKFrequent(int[] nums, int k) {
	    int[] frequency = new int[2000];
        for(int num: nums)
            frequency[num+1000]++;
        List<Integer> helperArray = new ArrayList<>();
        for (int num : nums)
            helperArray.add(num);   
        helperArray.sort((a,b) -> frequency[b+1000] - frequency[a+1000]);
        List<Integer> ans = new ArrayList<>();
        int count = 0;
        for(int i = 0; i < helperArray.size() && count < k; i++){
            if(!ans.contains(helperArray.get(i))){
                ans.add(helperArray.get(i));
                count++;
            }
                
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
