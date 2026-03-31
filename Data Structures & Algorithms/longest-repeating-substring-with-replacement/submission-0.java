class Solution {
    public int characterReplacement(String s, int k) {
        Set<Character> charSet = s.chars().mapToObj(c -> (char) c).collect(Collectors.toSet());
        Iterator<Character> itr = charSet.iterator();
        int maxLen = 0;
        while(itr.hasNext()){
            Character ch = itr.next();
            System.out.println("character: "+ch);
            LinkedList<Integer> swappedIndices = new LinkedList<>();
            int leftPointer = -1;
            int rightPointer = 0;
            int swapCount  = 0;
            int charMax = 0;
            while(rightPointer < s.length()){
                 if(s.charAt(rightPointer) != ch){
                    if(swapCount < k){
                        swapCount++;
                        swappedIndices.addLast(rightPointer);
                    }else{
                        System.out.println(ch);
                        swappedIndices.addLast(rightPointer);
                        leftPointer = swappedIndices.removeFirst();
                        
                    }
                }
                charMax = Math.max(rightPointer - leftPointer, charMax);
                rightPointer++;   
            }
            maxLen = Math.max(maxLen, charMax);
        }

        return maxLen;
    }
}
