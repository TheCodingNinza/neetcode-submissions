class Solution {
    class Pair {
        private int data;
        private int index;

        public Pair(int data, int index) {
            this.data = data;
            this.index = index;
        }
    }
    public int[] dailyTemperatures(int[] temperatures) {
        int[] ans = new int[temperatures.length];
        Stack<Pair> stk = new Stack<>();
        stk.push(new Pair(temperatures[0], 0));
        for(int i = 1; i < temperatures.length; i++){
            if(stk.peek().data > temperatures[i]){
                stk.push(new Pair(temperatures[i],i));
            }else{
                while(!stk.isEmpty() && stk.peek().data < temperatures[i]){
                    Pair pair = stk.pop();
                    ans[pair.index] = i - pair.index;
                }
                stk.push(new Pair(temperatures[i],i));
            }
        }
        return ans;
    }
}
