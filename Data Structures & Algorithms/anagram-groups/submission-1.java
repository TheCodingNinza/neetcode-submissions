class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<>();
        Map<Character, Integer> signatureMap = new TreeMap<>();
        Map<String, List<String>> groupingMap = new HashMap<>();
        for(String str: strs){
            signatureMap.clear();
            for(int i=0; i < str.length(); i++){
                signatureMap.put(str.charAt(i), signatureMap.getOrDefault(str.charAt(i), 0) + 1);
            }
            StringBuilder sign = new StringBuilder();
            for(Map.Entry<Character, Integer> entry: signatureMap.entrySet()){
                sign.append(entry.getKey());
                sign.append(entry.getValue());
            }
            groupingMap.computeIfAbsent(sign.toString(), x -> new ArrayList<>()).add(str); 
        }
        for(Map.Entry<String, List<String>> entry: groupingMap.entrySet()){
            groups.add(entry.getValue());
        }
        return groups;
    }
}
