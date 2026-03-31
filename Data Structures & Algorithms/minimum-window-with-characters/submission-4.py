class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_len = len(t)
        s_len = len(s)

        if t_len > s_len:
            return ""

        t_dict = {}
        s_dict = {}

        min_len = s_len
        ans = ""

        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1  

        for i in range(t_len, s_len+1):
            s_dict.clear()
            for j in range(0, i):
                s_dict[s[j]] = s_dict.get(s[j], 0) + 1
            if self.match(t_dict, s_dict):
                if i <= min_len:
                    ans = s[0:i]
                    min_len = i
            start = 0            
            for end in range(i , s_len):
                s_dict[s[end]] = s_dict.get(s[end], 0) + 1
                s_dict[s[start]] -= 1
                if s_dict[s[start]] == 0:
                    del s_dict[s[start]]
                start += 1    
                if self.match(t_dict, s_dict) == True:
                    if i <= min_len:
                        ans = s[start:end + 1]
                        min_len = i      

        return ans

    def match(self, t_dict: Dict[str, int],  s_dict: Dict[str, int]) -> bool:
        for key in t_dict:
            if key not in s_dict:
                return False
            if t_dict[key] > s_dict[key]:
                return False    
        return True        