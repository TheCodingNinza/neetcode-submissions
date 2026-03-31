class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int[] arrS = new int[26];
        int[] arrT = new int[26];

        for(int i = 0; i < s.length(); i++){
            int index  = (int) s.charAt(i) - (int) 'a';
            arrS[index]++;
            index  = (int) t.charAt(i) - (int ) 'a';
            arrT[index]++;
        }

        for(int i = 0; i < 26; i++){
            if(arrS[i] != arrT[i]){
                return false;
            }
        }

        return true;
        
    }
}
