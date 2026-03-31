class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False;

        s1_sign = [0] * 26
        s2_sign = [0] * 26


        for ch in s1:
            s1_sign[ord(ch) - ord('a')] += 1

        

        for i in range(n1):
            s2_sign[ord(s2[i]) - ord('a')] += 1

        print(s1_sign, s2_sign)
        if compare_sign(s1_sign, s2_sign):
            return True    

        left = 0
        for i in range(n1, n2):
            s2_sign[ord(s2[i]) - ord('a')] += 1
            s2_sign[ord(s2[left]) - ord('a')] -= 1
            print(s1_sign, s2_sign)
            if compare_sign(s1_sign, s2_sign):
                return True
            left += 1

        return False  
def compare_sign(s1_sign: list, s2_sign: list) -> bool:

    for i in range(26):
        if s1_sign[i] != s2_sign[i]:
            return False;

    return True;          