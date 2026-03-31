class Solution {
    public boolean hasDuplicate(int[] nums) {
            Set<Integer> st = new HashSet<>(Arrays.stream(nums).boxed().toList());;
            if(st.size() == nums.length)
                return false;
            else
                return true;
    }
}
