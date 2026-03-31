class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_len = len(t)
        s_len = len(s)

        if t_len > s_len:
            return ""

        t_dict = {}
        s_dict = {}

        ans = ""

        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        for i in range(0, t_len-1):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1  

        print(t_dict)
        print(s_dict)

        left = 0
        right = t_len - 1
        min_len = s_len + 1

        while right < s_len:
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            if self.match(t_dict, s_dict):
                while left <= right:
                    s_dict[s[left]] -= 1
                    if s_dict[s[left]] == 0:
                        del s_dict[s[left]]
                    if self.match(t_dict, s_dict) == False:
                        s_dict[s[left]] = s_dict.get(s[left], 0) + 1
                        break    
                    left += 1
                if min_len > (right - left + 1):
                    min_len = (right - left + 1)
                    ans = s[left:right+1]
            right += 1
        return ans                 
        

    def match(self, t_dict: Dict[str, int],  s_dict: Dict[str, int]) -> bool:
        for key in t_dict:
            if key not in s_dict:
                return False
            if t_dict[key] > s_dict[key]:
                return False    
        return True        