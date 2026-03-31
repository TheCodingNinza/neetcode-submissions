class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for strg in strs:
            encoded_str = encoded_str + strg + "€"
        print(f"encoded_str: {encoded_str}")    
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        curr_word = ""
        for ch in s:
            if ch != "€":
                curr_word += ch
            else:
                ans.append(curr_word)
                curr_word = ""
        return ans            