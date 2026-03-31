class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        unique_signature_str = dict()
        for strg in strs:
            char_freq_map = dict()
            for char in strg:
                char_freq_map[char] = char_freq_map.get(char, 0) + 1
            sign = ""   
            for key in sorted(char_freq_map):
                sign = sign + key + str(char_freq_map[key])
            if sign not in unique_signature_str:
                  unique_signature_str[sign] = []
            unique_signature_str[sign].append(strg)

        for key in unique_signature_str:
            ans.append(unique_signature_str[key])

        return ans        

        