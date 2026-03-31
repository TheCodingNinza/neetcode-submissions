class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 1
        n = len(s)

        char_list = list(set(s))

        for i in range(0, len(char_list)):
            
            curr_char = char_list[i]
            bal = k
            right = 0
            left = 0;

            while right < n:
                if s[right] == curr_char:
                    ans = max(ans, right - left + 1)
                else:
                    if bal > 0:
                        bal -= 1
                        ans = max(ans, right - left + 1)
                    else:
                        while left < n:
                            if s[left] != curr_char:
                                # bal += 1
                                left += 1
                                break
                            else:
                                left += 1    
                right += 1     

        return ans                    




