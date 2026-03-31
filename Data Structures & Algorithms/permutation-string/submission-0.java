class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Long> freqS1 = s1.chars().mapToObj(c -> (char) c).collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        int leftPointer = 0;
        int rightPointer = s1.length()-1;
        String initialString = s2.substring(leftPointer, rightPointer);
        Map<Character, Long> freqS2 = initialString.chars().mapToObj(ch -> (char) ch).collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        while(rightPointer < s2.length()){
            freqS2.put(s2.charAt(rightPointer), freqS2.getOrDefault(s2.charAt(rightPointer), 0L) + 1);
        
            if(hasSameSignature(freqS1, freqS2))
                return true;
            freqS2.put(s2.charAt(leftPointer), freqS2.get(s2.charAt(leftPointer)) - 1);
            if(freqS2.get(s2.charAt(leftPointer)) == 0){
                freqS2.remove(s2.charAt(leftPointer));
            }    
            rightPointer++;
            leftPointer++;    
        }
        return false;
    }

    private boolean hasSameSignature(Map<Character, Long> freqS1, Map<Character, Long> freqS2){
        if(freqS1.size() != freqS2.size())
            return false;

        for(Map.Entry<Character, Long> entry: freqS1.entrySet()){
            if(!freqS2.containsKey(entry.getKey()))
                return false;
            else{
                if(entry.getValue() != freqS2.get(entry.getKey()))
                    return false;
            }
        }

        return true;    
    }
}
