class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            char currChar = s.charAt(i);
            if(currChar == '(' || currChar == '{' || currChar == '['){
                stk.push(currChar);
            }else{
                if(stk.isEmpty())
                    return false;
                char topChar = stk.pop();
                if(topChar == '(' && currChar == ')'){

                }else if(topChar == '[' && currChar == ']'){

                }else if(topChar == '{' && currChar == '}'){

                }else{
                    return false;
                }
            }
        }
        if(!stk.isEmpty())
            return false;
        return true;
    }
}
