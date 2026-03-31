class Solution {
    
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deq = new LinkedList<>();
        int index = 0;
        int[] ans = new int[nums.length - k + 1];
        for(int i=0; i < nums.length; i++){
            int currNum = nums[i];
            while(!deq.isEmpty() && currNum > nums[deq.peekLast()]){
                deq.pollLast();
            }
            deq.addLast(i);
            System.out.println(deq);
            if(i >= k-1){
                ans[index] = nums[deq.peekFirst()];
                index++;
                if(deq.peekFirst() == i - k + 1)
                    deq.pollFirst();
            }
        }
        return ans;
    }
}
