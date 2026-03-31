class Solution {
    public int[] topKFrequent(int[] nums, int k) {
	    int[] ans = new int[k];
        Map<Integer, List<Integer>> reverseTreeMap = new TreeMap<>((a, b) -> b - a);	
	    Map<Integer, Integer> map = new HashMap<>(); 
 	    
        for(int num: nums){
	        map.put(num, map.getOrDefault(num, 0)+ 1);
        }

        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
	        reverseTreeMap.computeIfAbsent(entry.getValue(), x -> new ArrayList<>()).add(entry.getKey());
        }
        
        int count = 0;


        for(Map.Entry<Integer, List<Integer>> entry: reverseTreeMap.entrySet()){
            if(count < k){
                for(int num: entry.getValue()){
                    if(count >= k)
                        break;
                    ans[count] = num;
                    count++;
                }
            }else{
                break;
            }
        }


        return ans;

    }
}
