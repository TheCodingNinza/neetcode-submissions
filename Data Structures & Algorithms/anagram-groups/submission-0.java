class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
            List<List<String>> ans = new ArrayList<>();
            Set<String> done = new HashSet<>();
            Map<String, int[]> memory = new HashMap<>();
            for(int i = 0; i < strs.length; i++){
                if(done.contains(strs[i]))
                    continue;
                int[] fingerPrint = new int[26];
                if(!memory.containsKey(strs[i])){
                    calculateFingerPrint(strs[i], fingerPrint);
                    memory.put(strs[i], fingerPrint);
                }
                else
                    fingerPrint = memory.get(strs[i]);
                List<String> temp = new ArrayList<>();
                temp.add(strs[i]);
                done.add(strs[i]);
                for(int j = i + 1; j < strs.length; j++){
                    int[] carbonPrint = new int[26];
                    if(!memory.containsKey(strs[j])){
                        calculateFingerPrint(strs[j], carbonPrint);
                        memory.put(strs[j], carbonPrint);
                    }
                    else
                        carbonPrint = memory.get(strs[j]);
                    if(compare(fingerPrint, carbonPrint)){
                        temp.add(strs[j]);
                        done.add(strs[j]);
                    }
                }
                ans.add(temp);
            }
            return ans;      
        }


    public void calculateFingerPrint(String str, int[] fingerPrint){
        for(int k = 0; k < str.length(); k++){
            int key = (int)str.charAt(k) - (int)'a';
            fingerPrint[key]++;
        }
    }


    public boolean compare(int[] a, int[] b){
        for(int i = 0; i < 26; i++){
            if(a[i] != b[i])
                return false;
        }
        return true;
    }
}
