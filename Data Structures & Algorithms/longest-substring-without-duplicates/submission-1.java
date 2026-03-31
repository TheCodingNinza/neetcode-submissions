class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeenMap = new HashMap<>();
        int leftPointer = -1;
        int rightPointer = 0;
        int maxLen = 0;
        while(rightPointer < s.length()){
            Character currChar = s.charAt(rightPointer);
            // System.out.println("currChar: "+currChar);
            if(lastSeenMap.containsKey(currChar) && lastSeenMap.get(currChar) > leftPointer){
                leftPointer = lastSeenMap.get(currChar);    
            }
            lastSeenMap.put(currChar, rightPointer);
           
            // System.out.println("rightPointer: "+rightPointer);
            //  System.out.println("leftPointer: "+leftPointer);
            // System.out.println("diff: "+ (rightPointer - leftPointer));
            maxLen = Math.max(rightPointer - leftPointer, maxLen);
            rightPointer++;
        }
        return maxLen;
    }
}
