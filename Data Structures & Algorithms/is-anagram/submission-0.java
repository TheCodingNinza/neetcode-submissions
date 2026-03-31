class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        char[] arrS = new char[26];
        char[] arrT = new char[26];

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
