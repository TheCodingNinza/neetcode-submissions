class Solution {
    public boolean isPalindrome(String s) {
        s = s.chars()
         .filter(Character::isLetterOrDigit)
         .map(Character::toLowerCase)
         .collect(StringBuilder::new,
                  StringBuilder::appendCodePoint,
                  StringBuilder::append)
         .toString();
        System.out.println(s);
        int leftPointer = 0;
        int rightPointer = s.length() - 1;
        while(leftPointer <= rightPointer){
            if(s.charAt(leftPointer) != s.charAt(rightPointer)){
                return false;
            }
            leftPointer++;
            rightPointer--;
        }
        return true;
    }
}
