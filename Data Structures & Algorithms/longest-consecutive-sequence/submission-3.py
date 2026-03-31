class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0;
        nums.sort()
        for i in range(len(nums)):
            start = nums[i] 
            count = 1
            for j in range(i+1, len(nums), 1):
                if nums[j] == start + 1:
                    count += 1
                    start += 1        
            ans = max(ans, count)
    
        return ans
