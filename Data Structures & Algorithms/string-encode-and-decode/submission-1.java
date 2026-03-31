class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        if(strs.isEmpty())
            return null;
        else {
            encoded.append(strs.get(0));
        }
        for(int i=1 ; i < strs.size(); i++){
            encoded.append("\n");
            encoded.append(strs.get(i));
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        if(str == null)
            return new ArrayList<>();
        return Arrays.stream(str.split("\n")).toList();
    }
}
