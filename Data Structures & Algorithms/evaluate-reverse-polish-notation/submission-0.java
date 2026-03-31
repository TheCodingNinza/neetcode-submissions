class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<>();
        Set<String> operators = new HashSet<>();
        operators.add("+");
        operators.add("*");
        operators.add("-");
        operators.add("/");
        for(String token: tokens){
            if(operators.contains(token)){
                int operand2 = stk.pop();
                int operand1 = stk.pop();
                if(token.equals("*"))
                    stk.push(operand1 * operand2);
                else if(token.equals("/"))
                    stk.push(operand1 / operand2);
                else if(token.equals("+"))
                    stk.push(operand1 + operand2);
                else
                    stk.push(operand1 - operand2);
            }else
                stk.push(Integer.parseInt(token));
        }
        return stk.pop();
    }
}
