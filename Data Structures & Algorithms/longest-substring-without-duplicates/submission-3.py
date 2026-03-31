class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        left = 0
        right = 1
        ans = 1;
        
        while right < n:
            val = s.find(s[right], left, right)
            if(val != -1):
                left = val + 1  
            ans = max(ans, right - left + 1)
            right += 1 
            

        return ans;    
